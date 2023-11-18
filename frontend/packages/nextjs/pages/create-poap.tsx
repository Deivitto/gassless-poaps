import Link from "next/link";
import React from 'react';
import AddPropertyForm from '../components/Form';
import type { NextPage } from "next";
import { BugAntIcon, MagnifyingGlassIcon, PlusCircleIcon, SparklesIcon, UserIcon } from "@heroicons/react/24/outline";
import { MetaHeader } from "~~/components/MetaHeader";

const handleAddProperty = (propertyData: { propertyName: string; propertyId: string; quantity: number }) => {
  // Implement the logic to add ERC-1155 property
  // For example, you might want to store the properties in state or send them to an API.

  console.log('Adding ERC1155:', propertyData);

  // Add your logic here to handle the property data, such as making an API call to store it.
};

const CreatePoap: NextPage = () => {
  return (
    <>
      <MetaHeader  title="Wine & POAPs"
        description="Create events and mint gasless POAPs!"/>
      <div className="flex items-center flex-col flex-grow pt-10">
        <div className="px-5">
          <h1 className="text-center mb-8">
            <span className="block text-4xl mt-2 mb-2 font-bold">GaslessPOAPs</span>
            <span className="block text-2xl mt-2 mb-2">Create your events, join events and receive POAPs!</span>
          </h1>
        </div>

        <AddPropertyForm onSubmit={handleAddProperty} />
        <div className="flex-grow bg-base-300 w-full mt-16 px-8 py-12">
          <div className="flex justify-center items-center gap-12 flex-col sm:flex-row">
            {/* Display your existing properties here if any */}

          </div>
        </div>
      </div>
    </>
  );
};

export default CreatePoap;
