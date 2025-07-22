import React, { useEffect, useState } from 'react';
import { fetchReceipts } from '../services/api';
import { Bar, Line } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
} from 'chart.js';

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);

export default function Charts() {
  const [chartData, setChartData] = useState({});

  useEffect(() => {
    async function buildData() {
      const records = await fetchReceipts();
      const byVendor = {};
      const byDate = {};

      records.forEach(r => {
        byVendor[r.vendor] = (byVendor[r.vendor] || 0) + r.amount;
        const month = r.date.slice(0, 7);
        byDate[month] = (byDate[month] || 0) + r.amount;
      });

      setChartData({
        vendorData: {
          labels: Object.keys(byVendor),
          datasets: [{ label: 'Spend by Vendor', data: Object.values(byVendor) }]
        },
        timeData: {
          labels: Object.keys(byDate),
          datasets: [{ label: 'Monthly Spend', data: Object.values(byDate) }]
        }
      });
    }
    buildData();
  }, []);

  if (!chartData.vendorData) return null;

  return (
    <div className="charts">
      <div className="chart">
        <h3>Spend by Vendor</h3>
        <Bar data={chartData.vendorData} />
      </div>
      <div className="chart">
        <h3>Monthly Spend</h3>
        <Line data={chartData.timeData} />
      </div>
    </div>
  );
}