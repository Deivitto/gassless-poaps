import Link from "next/link";
import type { NextPage } from "next";
import { BugAntIcon, MagnifyingGlassIcon, PlusCircleIcon, SparklesIcon, UserIcon } from "@heroicons/react/24/outline";
import { MetaHeader } from "~~/components/MetaHeader";

const Home: NextPage = () => {
  return (
    <>
      <MetaHeader  title="Wine & POAPs"
        description="Create events and mint gasless POAPs!"/>
      <div className="flex items-center flex-col flex-grow pt-10">
        <div className="px-5">
          <h1 className="text-center mb-8">
            {/* <span className="block text-2xl mb-2">Wine and </span> */}
            <span className="block text-4xl mt-2 mb-2 font-bold">GaslessPOAPs</span>
            <span className="block text-2xl mt-2 mb-2">Create your events, join events and receive POAPs!</span>
          </h1>
          {/* <p className="text-center text-lg">
            Get started by editing{" "}
            <code className="italic bg-base-300 text-base font-bold">packages/nextjs/pages/index.tsx</code>
          </p>
          <p className="text-center text-lg">
            Edit your smart contract <code className="italic bg-base-300 text-base font-bold">YourContract.sol</code> in{" "}
            <code className="italic bg-base-300 text-base font-bold">packages/hardhat/contracts</code>
          </p> */}
        </div>

        <div className="flex-grow bg-base-300 w-full mt-16 px-8 py-12">
          <div className="flex justify-center items-center gap-12 flex-col sm:flex-row">
            <div className="flex flex-col bg-base-100 px-10 py-10 text-center items-center max-w-xs rounded-3xl">
              <PlusCircleIcon className="h-8 w-8 fill-secondary" />
              <p>
                <Link href="/create-poap" passHref className="link">
                Create events{" "}
                  {/* Debug Contract */}
                </Link>{" "}
              </p>
            </div>
            <div className="flex flex-col bg-base-100 px-10 py-10 text-center items-center max-w-xs rounded-3xl">
              <UserIcon className="h-8 w-8 fill-secondary" />
              <p>
                <Link href="/mint-poap" passHref className="link">
                Join an event{" "}
                </Link>{" "}
              </p>
            </div>
            {/* <div className="flex flex-col bg-base-100 px-10 py-10 text-center items-center max-w-xs rounded-3xl">
              <MagnifyingGlassIcon className="h-8 w-8 fill-secondary" />
              <p>
                Some action we still don't know{" "}
                <Link href="/blockexplorer" passHref className="link">
                </Link>{" "}
              </p>
            </div> */}
          </div>
        </div>
      </div>
    </>
  );
};

export default Home;
