// components/AddPropertyForm.tsx
import React, { useState } from 'react';

interface PropertyFormProps {
  onSubmit: (propertyData: PropertyData) => void;
}

interface PropertyData {

}

const AddPropertyForm: React.FC<PropertyFormProps> = ({ onSubmit }) => {

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();

    onSubmit({

    });
  };

  return (
    <form onSubmit={handleSubmit} className='flex flex-col custom_form'>
      <h1 className='mb-2'>Mint your POAP!</h1>
      <button className="btn" type="submit">Mint</button>
    </form>
  );
};

export default AddPropertyForm;
