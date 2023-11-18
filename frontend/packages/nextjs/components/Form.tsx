// components/AddPropertyForm.tsx
import React, { useState } from 'react';

interface PropertyFormProps {
  onSubmit: (propertyData: PropertyData) => void;
}

interface PropertyData {
  propertyId: string;
  quantity: number;
  imageUrl: string;
  deadline: string; // uint40 represented as a string
  name: string;
  description: string;
}

const AddPropertyForm: React.FC<PropertyFormProps> = ({ onSubmit }) => {
  const [propertyId, setPropertyId] = useState('');
  const [quantity, setQuantity] = useState('');
  const [imageUrl, setImageUrl] = useState('');
  const [deadline, setDeadline] = useState('');
  const [name, setName] = useState('');
  const [description, setDescription] = useState('');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();

    if (!propertyId || !quantity || !imageUrl || !deadline || !name || !description) {
      alert('Please fill in all fields');
      return;
    }

    onSubmit({
      propertyId,
      quantity: parseInt(quantity, 10),
      imageUrl,
      deadline,
      name,
      description,
    });

    setPropertyId('');
    setQuantity('');
    setImageUrl('');
    setDeadline('');
    setName('');
    setDescription('');
  };

  return (
    <form onSubmit={handleSubmit} className='flex flex-col custom_form'>
      <h1>Your ERC-1155 Properties</h1>

      <div className='mb-1 mt-2'>
        Name:
      </div>
      <input
        type="text"
        className='mb-2 mt-2 input'
        value={name}
        onChange={(e) => setName(e.target.value)}
      />

      <div className='mb-1 mt-2'>
        Description:
      </div>
      <textarea
        className='mb-2 mt-2 input'
        value={description}
        onChange={(e) => setDescription(e.target.value)}
      />

        <div className='mb-1 mt-2'>
            Quantity:
        </div>
        <input
          type="number"
          className='mb-2 mt-2 input'
          value={quantity}
          onChange={(e) => setQuantity(e.target.value)}
        />

        {/* New fields */}
        <div className='mb-1 mt-2'>
        Deadline (uint40):
      </div>
      <input
        type="text"
        className='mb-2 mt-2 input'
        value={deadline}
        onChange={(e) => setDeadline(e.target.value)}
      />


      <div className='mb-1 mt-2'>Image:</div>
      <label className="custom-file-upload">
          Select image: {imageUrl}

            <input
              type="file"
              className='mb-2 mt-2 input fileType'
              value={imageUrl}
              onChange={(e) => setImageUrl(e.target.value)}
            />
      </label>

      <button className="btn" type="submit">Add POAP Event</button>
    </form>
  );
};

export default AddPropertyForm;
