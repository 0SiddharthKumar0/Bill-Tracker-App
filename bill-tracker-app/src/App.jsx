import React from 'react';
import UploadForm from './components/UploadForm';
import RecordsTable from './components/RecordsTable';
import Charts from './components/Charts';
import './App.css';

function App() {
  return (
    <div className="container">
      <h1>Bill Tracker App</h1>
      <UploadForm />
      <RecordsTable />
      <Charts />
    </div>
  );
}

export default App;