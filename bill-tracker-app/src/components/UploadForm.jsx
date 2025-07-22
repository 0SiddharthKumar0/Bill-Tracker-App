import React, { useState } from 'react';
import { uploadReceipt } from '../services/api';

export default function UploadForm() {
  const [file, setFile] = useState(null);
  const [error, setError] = useState('');
  const [success, setSuccess] = useState(null);

  const handleChange = (e) => {
    setFile(e.target.files[0]);
    setError('');
    setSuccess(null);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!file) {
      setError('Please select a file first.');
      return;
    }
    try {
      const data = await uploadReceipt(file);
      setSuccess(data.receipt);
    } catch (err) {
      setError(err.response?.data?.detail || 'Upload failed.');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input type="file" accept=".png,.jpg,.jpeg,.pdf,.txt" onChange={handleChange} />
      <button type="submit">Upload Receipt</button>
      { error && <p className="error">{error}</p> }
      { success && (
        <div className="receipt-success">
          <h4>Parsed Receipt:</h4>
          <pre>{JSON.stringify(success, null, 2)}</pre>
        </div>
      )}
    </form>
  );
}