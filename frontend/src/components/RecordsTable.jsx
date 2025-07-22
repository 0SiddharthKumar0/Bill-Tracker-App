import React, { useEffect, useState } from 'react';
import { fetchReceipts } from '../services/api';

export default function RecordsTable() {
  const [records, setRecords] = useState([]);

  useEffect(() => {
    async function load() {
      try {
        const data = await fetchReceipts();
        setRecords(data);
      } catch (err) {
        console.error('Failed to load receipts:', err);
      }
    }
    load();
  }, []);

  if (!records.length) return <p>No receipts yet.</p>;

  return (
    <table className="records-table">
      <thead>
        <tr>
          <th>ID</th>
          <th>Vendor</th>
          <th>Date</th>
          <th>Amount</th>
          <th>Category</th>
        </tr>
      </thead>
      <tbody>
        {records.map(r => (
          <tr key={r.id}>
            <td>{r.id}</td>
            <td>{r.vendor}</td>
            <td>{new Date(r.date).toLocaleDateString()}</td>
            <td>{r.amount.toFixed(2)}</td>
            <td>{r.category || '—'}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}