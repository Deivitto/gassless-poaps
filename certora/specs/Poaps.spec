//certoraRun certora/configuration/Poaps.conf --packages @openzeppelin=lib/openzeppelin-contracts

// There is a spec for ERC1155 in the OpenZeppelin repo, but it is in CVL 1.
// https://github.com/Certora/openzeppelin-contracts/blob/master/certora/specs/ERC1155.spec

methods {
    function isApprovedForAll(address, address) external returns(bool) envfree;
    function balanceOf(address, uint256) external returns(uint256) envfree;
    function balanceOfBatch(address[], uint256[]) external returns(uint256[]) envfree;
    //function _doSafeBatchTransferAcceptanceCheck(address, address, address, uint256[], uint256[], bytes) external envfree;
    //function _doSafeTransferAcceptanceCheck(address, address, address, uint256, uint256, bytes) external envfree;

    function setApprovalForAll(address, bool) external;
    function safeTransferFrom(address, address, uint256, uint256, bytes) external;
    function safeBatchTransferFrom(address, address, uint256[], uint256[], bytes) external;
    //function mint(address, uint256, uint256, bytes) external;
    function mint(uint256, address, uint56, bytes) external;
    //function mintBatch(address, uint256[], uint256[], bytes) external;
    //function burn(address, uint256, uint256) external;
    //function burnBatch(address, uint256[], uint256[]) external;
}



/////////////////////////////////////////////////
// Approval (4/4)
/////////////////////////////////////////////////

// Function $f, which is not setApprovalForAll, should not change approval
// certoraRun certora/configuration/Poaps.conf  --rule unexpectedAllowanceChange --packages @openzeppelin=lib/openzeppelin-contracts
rule unexpectedAllowanceChange(method f, env e) filtered { f -> f.selector != sig:setApprovalForAll(address, bool).selector } {
    address account; address operator;
    bool approveBefore = isApprovedForAll(account, operator); 

    calldataarg args;
    f(e, args);

    bool approveAfter = isApprovedForAll(account, operator);

    assert approveBefore == approveAfter, "You couldn't get king's approval this way!";
}   

// approval can be changed only by owner
// certoraRun certora/configuration/Poaps.conf  --rule onlyOwnerCanApprove --packages @openzeppelin=lib/openzeppelin-contracts
rule onlyOwnerCanApprove(env e){
    address owner; address operator; bool approved;

    bool aprovalBefore = isApprovedForAll(owner, operator);

    setApprovalForAll(e, operator, approved);

    bool aprovalAfter = isApprovedForAll(owner, operator);

    assert aprovalBefore != aprovalAfter => owner == e.msg.sender, "There should be only one owner";
}

// Chech that isApprovedForAll() revertes in planned scenarios and no more. 
// certoraRun certora/configuration/Poaps.conf  --rule approvalRevertCases --packages @openzeppelin=lib/openzeppelin-contracts
rule approvalRevertCases(env e){
    address account; address operator;
    isApprovedForAll@withrevert(account, operator);
    assert !lastReverted, "Houston, we have a problem";
}

// setApproval changes only one approval
// certoraRun certora/configuration/Poaps.conf  --rule onlyOneAllowanceChange --packages @openzeppelin=lib/openzeppelin-contracts
rule onlyOneAllowanceChange(method f, env e) {
    address owner; address operator; address user; 
    bool approved;

    bool userApproveBefore = isApprovedForAll(owner, user);

    setApprovalForAll(e, operator, approved);

    bool userApproveAfter = isApprovedForAll(owner, user);

    assert userApproveBefore != userApproveAfter => (e.msg.sender == owner && operator == user), "Imposter!";
}  

/////////////////////////////////////////////////
// Balance (3/3)
/////////////////////////////////////////////////

// Function $f, which is not one of transfers, mints and burns, should not change balanceOf of a user
// certoraRun certora/configuration/Poaps.conf  --rule unexpectedBalanceChange --packages @openzeppelin=lib/openzeppelin-contracts
rule unexpectedBalanceChange(method f, env e) 
    filtered { f -> f.selector != sig:safeTransferFrom(address, address, uint256, uint256, bytes).selector
                        && f.selector != sig:safeBatchTransferFrom(address, address, uint256[], uint256[], bytes).selector 
                        && f.selector != sig:mint(uint256, address, uint56, bytes).selector 
                        //&& f.selector != sig:mintBatch(address, uint256[], uint256[], bytes).selector  
                        //&& f.selector != sig:burn(address, uint256, uint256).selector 
                        //&& f.selector != sig:burnBatch(address, uint256[], uint256[]).selector 
                        } {
    address from; uint256 id;
    uint256 balanceBefore = balanceOf(from, id);

    calldataarg args;
    f(e, args);

    uint256 balanceAfter = balanceOf(from, id);

    assert balanceBefore == balanceAfter, "How you dare to take my money?";
}   

// Chech that `balanceOf()` revertes in planned scenarios and no more (only if `account` is 0)
// certoraRun certora/configuration/Poaps.conf  --rule balanceOfRevertCases --packages @openzeppelin=lib/openzeppelin-contracts
rule balanceOfRevertCases(env e){
    address account; uint256 id;
    balanceOf@withrevert(account, id);
    assert lastReverted => account == 0, "Houston, we have a problem";
}

// Chech that `balanceOfBatch()` revertes in planned scenarios and no more (only if at least one of `account`s is 0)
// certoraRun certora/configuration/Poaps.conf  --rule balanceOfBatchRevertCases --packages @openzeppelin=lib/openzeppelin-contracts
// warning: vacuity check failed (the rule is vacuous)
rule balanceOfBatchRevertCases(env e){
    address[] accounts; uint256[] ids;
    address account1; address account2; address account3;
    uint256 id1; uint256 id2; uint256 id3;

    require accounts.length == 3; 
    require ids.length == 3; 

    require accounts[0] == account1; require accounts[1] == account2; require accounts[2] == account3;

    balanceOfBatch@withrevert(accounts, ids);
    assert lastReverted => (account1 == 0 || account2 == 0 || account3 == 0), "Houston, we have a problem";
}

/////////////////////////////////////////////////
// Transfer (13/13)
/////////////////////////////////////////////////

// transfer additivity
// certoraRun certora/configuration/Poaps.conf  --rule transferAdditivity --packages @openzeppelin=lib/openzeppelin-contracts
rule transferAdditivity(env e){
    address from; address to; uint256 id; bytes data;
    uint256 amount; uint256 amount1; uint256 amount2;
    //require amount == assert_uint256(amount1 + amount2);
    require amount == require_uint256(amount1 + amount2);

    storage initialStorage = lastStorage;

    safeTransferFrom(e, from, to, id, amount, data);

    uint256 balanceAfterSingleTransaction = balanceOf(to, id);

    safeTransferFrom(e, from, to, id, amount1, data) at initialStorage;
    safeTransferFrom(e, from, to, id, amount2, data);

    uint256 balanceAfterDoubleTransaction = balanceOf(to, id);

    assert balanceAfterSingleTransaction == balanceAfterDoubleTransaction, "Not additive";
}

// safeTransferFrom updates `from` and `to` balances
// certoraRun certora/configuration/Poaps.conf  --rule transferCorrectness --packages @openzeppelin=lib/openzeppelin-contracts
rule transferCorrectness(env e){
    address from; address to; uint256 id; uint256 amount; bytes data;

    require to != from;

    mathint fromBalanceBefore = balanceOf(from, id);
    mathint toBalanceBefore = balanceOf(to, id);

    safeTransferFrom(e, from, to, id, amount, data);

    mathint fromBalanceAfter = balanceOf(from, id);
    mathint toBalanceAfter = balanceOf(to, id);

    assert fromBalanceBefore == fromBalanceAfter + amount, "Something wet wrong";
    assert toBalanceBefore == toBalanceAfter - amount, "Something wet wrong";
}

// safeBatchTransferFrom updates `from` and `to` balances)
// certoraRun certora/configuration/Poaps.conf  --rule transferBatchCorrectness --packages @openzeppelin=lib/openzeppelin-contracts
// warning: vacuity check failed (the rule is vacuous):
rule transferBatchCorrectness(env e){
    address from; address to; uint256[] ids; uint256[] amounts; bytes data;
    uint256 idToCheck1; uint256 amountToCheck1;
    uint256 idToCheck2; uint256 amountToCheck2;
    uint256 idToCheck3; uint256 amountToCheck3;

    require to != from;
    require idToCheck1 != idToCheck2 && idToCheck3 != idToCheck2 && idToCheck1 != idToCheck3;
    
    require ids.length == 3;        
    require amounts.length == 3;    
    require ids[0] == idToCheck1; require amounts[0] == amountToCheck1;
    require ids[1] == idToCheck2; require amounts[1] == amountToCheck2;
    require ids[2] == idToCheck3; require amounts[2] == amountToCheck3;

    mathint fromBalanceBefore1 = balanceOf(from, idToCheck1);
    mathint fromBalanceBefore2 = balanceOf(from, idToCheck2);
    mathint fromBalanceBefore3 = balanceOf(from, idToCheck3);

    mathint toBalanceBefore1 = balanceOf(to, idToCheck1);
    mathint toBalanceBefore2 = balanceOf(to, idToCheck2);
    mathint toBalanceBefore3 = balanceOf(to, idToCheck3);

    safeBatchTransferFrom(e, from, to, ids, amounts, data);

    mathint fromBalanceAfter1 = balanceOf(from, idToCheck1);
    mathint fromBalanceAfter2 = balanceOf(from, idToCheck2);
    mathint fromBalanceAfter3 = balanceOf(from, idToCheck3);

    mathint toBalanceAfter1 = balanceOf(to, idToCheck1);
    mathint toBalanceAfter2 = balanceOf(to, idToCheck2);
    mathint toBalanceAfter3 = balanceOf(to, idToCheck3);

    assert (fromBalanceBefore1 == fromBalanceAfter1 + amountToCheck1)
                && (fromBalanceBefore2 == fromBalanceAfter2 + amountToCheck2)
                && (fromBalanceBefore3 == fromBalanceAfter3 + amountToCheck3), "Something wet wrong";
    assert (toBalanceBefore1 == toBalanceAfter1 - amountToCheck1)
                && (toBalanceBefore2 == toBalanceAfter2 - amountToCheck2)
                && (toBalanceBefore3 == toBalanceAfter3 - amountToCheck3), "Something wet wrong";
}

// cannot transfer more than `from` balance (safeTransferFrom version)
// certoraRun certora/configuration/Poaps.conf  --rule cannotTransferMoreSingle --packages @openzeppelin=lib/openzeppelin-contracts
rule cannotTransferMoreSingle(env e){
    address from; address to; uint256 id; uint256 amount; bytes data;
    uint256 balanceBefore = balanceOf(from, id);

    safeTransferFrom@withrevert(e, from, to, id, amount, data);

    assert amount > balanceBefore => lastReverted, "Achtung! Scammer!";
}

// cannot transfer more than allowed (safeBatchTransferFrom version)
// certoraRun certora/configuration/Poaps.conf  --rule cannotTransferMoreSingle --packages @openzeppelin=lib/openzeppelin-contracts
rule cannotTransferMoreBatch(env e){
    address from; address to; uint256[] ids; uint256[] amounts; bytes data;
    uint256 idToCheck1; uint256 amountToCheck1;
    uint256 idToCheck2; uint256 amountToCheck2;
    uint256 idToCheck3; uint256 amountToCheck3;

    uint256 balanceBefore1 = balanceOf(from, idToCheck1);
    uint256 balanceBefore2 = balanceOf(from, idToCheck2);
    uint256 balanceBefore3 = balanceOf(from, idToCheck3);

    require ids.length == 3;        
    require amounts.length == 3;    
    require ids[0] == idToCheck1; require amounts[0] == amountToCheck1;
    require ids[1] == idToCheck2; require amounts[1] == amountToCheck2;
    require ids[2] == idToCheck3; require amounts[2] == amountToCheck3;

    safeBatchTransferFrom@withrevert(e, from, to, ids, amounts, data);

    assert (amountToCheck1 > balanceBefore1 || amountToCheck2 > balanceBefore2 || amountToCheck3 > balanceBefore3) => lastReverted, "Achtung! Scammer!";
}

// Sender calling safeTransferFrom should only reduce 'from' balance and not other's if sending amount is greater than 0
// certoraRun certora/configuration/Poaps.conf  --rule cannotTransferMoreSingle 
rule transferBalanceReduceEffect(env e){
    address from; address to; address other;
    uint256 id; uint256 amount; 
    bytes data;

    require other != to;

    uint256 otherBalanceBefore = balanceOf(other, id);

    safeTransferFrom(e, from, to, id, amount, data);

    uint256 otherBalanceAfter = balanceOf(other, id);

    assert from != other => otherBalanceBefore == otherBalanceAfter, "Don't touch my money!";
}