import Link from "next/link";
import React from 'react';
import AddPropertyForm from '../components/Form';
import type { NextPage } from "next";
import { BugAntIcon, MagnifyingGlassIcon, PlusCircleIcon, SparklesIcon, UserIcon } from "@heroicons/react/24/outline";
import { MetaHeader } from "~~/components/MetaHeader";
import CreatePoap from "./create-poap";
import PoapMinter from "~~/components/PoapMinter";

const handleAddProperty = (propertyData: { propertyName: string; propertyId: string; quantity: number }) => {
  // Implement the logic to add ERC-1155 property
  // For example, you might want to store the properties in state or send them to an API.

  console.log('Adding property:', propertyData);

  // Add your logic here to handle the property data, such as making an API call to store it.
};

const MintPoap: NextPage = () => {
  return (
    <>
      <MetaHeader  title="GaslessPOAPs"
        description="Create events and mint gasless POAPs!"/>
      <div className="flex items-center flex-col flex-grow pt-10">
        <div className="px-5">
          <h1 className="text-center mb-8">
            <span className="block text-4xl mt-2 mb-2 font-bold">GaslessPoaps</span>
            <span className="block text-2xl mt-2 mb-2">Create your events, join events and receive POAPs!</span>
          </h1>
        </div>

        <PoapMinter onSubmit={handleAddProperty} />
      </div>
    </>
  );
};

export default MintPoap;
