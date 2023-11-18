# Smart Wallet

## Frontend Quickstart

To get started with Scaffold-ETH 2, follow the steps below:

1. Clone this repo & install dependencies

```
cd scaffold-eth-2
yarn install
foundryup
```

2. Create your `.env` file inside `packages/foundry`:

```
(echo "DEPLOYER_PRIVATE_KEY=";  echo "ALCHEMY_API_KEY=oKxs-03sij-U_N0iOlrSsZFr29-IqbuF"; echo "ETHERSCAN_API_KEY=DNXJA8RX2Q3VZ4URQIWP7Z68CJXQZSC6AW") >> packages/foundry/.env
```

3. Run a local network in the first terminal:

```
yarn chain
```

This command starts a local Ethereum network using Anvil in Foundry. The network runs on your local machine and can be used for testing and development. You can customize the network configuration in `foundry.toml`

4. On a second terminal, deploy the test contract:

```
yarn deploy
```

This command deploys a test smart contract to the local network. The contract is located in `packages/foundry/src` and can be modified to suit your needs. The `yarn deploy` command uses the deploy script located in `packages/foundry/script/Deploy.s.sol` to deploy the contract to the network. You can also customize the deploy script.

5. On a third terminal, start your NextJS app:

```
yarn start
```

Visit your app on: `http://localhost:3000`. You can interact with your smart contract using the contract component or the example ui in the frontend. You can tweak the app config in `packages/nextjs/scaffold.config.ts`.

Run smart contract test with `yarn foundry:test`

- Edit your smart contract `YourContract.sol` in `packages/foundry/src`
- Edit your frontend in `packages/nextjs/pages`
- Edit your deployment scripts in `packages/foundry/script/Deploy.s.sol`

- Adding custom policy stuff
    - circuit breaker?
    - can this wallet belong to a big entity?
    - multi signature




## Links
- RIP 7560 https://github.com/ethereum/RIPs/pull/3/files
- https://github.com/eth-infinitism/account-abstraction
