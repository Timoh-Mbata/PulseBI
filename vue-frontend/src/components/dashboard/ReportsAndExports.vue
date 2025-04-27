<template>
  <div class="reports-container">
    <h2 class="title">Reports & Exports</h2>
    
    <!-- Export Buttons -->
    <div class="buttons-container">
      <button @click="exportPDF" class="export-button pdf-button">
        Export PDF
      </button>
      <button @click="exportCSV" class="export-button csv-button">
        Export CSV
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import jsPDF from 'jspdf'; // Library for generating PDFs
import { saveAs } from 'file-saver'; // For saving files locally
import { parse } from 'json2csv'; // For converting JSON to CSV

// Example data to be exported
const liveStats = ref([
  { label: 'Live Sales', value: '120' },
  { label: 'Site Traffic', value: '865' },
  { label: 'Active Users', value: '42' },
]);

// Function to export data as PDF
const exportPDF = () => {
  const doc = new jsPDF();

  doc.setFontSize(16);
  doc.text('Live Data Report', 20, 20);
  doc.setFontSize(12);

  let yOffset = 30;
  liveStats.value.forEach((item) => {
    doc.text(`${item.label}: ${item.value}`, 20, yOffset);
    yOffset += 10;
  });

  // Save PDF
  doc.save('live_data_report.pdf');
};

// Function to export data as CSV
const exportCSV = () => {
  // Convert data to CSV format
  const csvData = parse(liveStats.value);
  
  // Create a Blob and trigger download
  const blob = new Blob([csvData], { type: 'text/csv;charset=utf-8;' });
  saveAs(blob, 'live_data_report.csv');
};
</script>

<style scoped>
/* Container for the whole report section */
.reports-container {
  background: linear-gradient(135deg, #f5f7fa, #c3cfe2); /* Light gradient background */
  padding: 30px;
  border-radius: 15px;
  box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.1);
  width: 100%;
  max-width: 600px;
  margin: 20px auto;
  transition: transform 0.3s ease-in-out;
}

/* Title styling */
.title {
  font-size: 24px;
  font-weight: bold;
  color: #2c3e50;
  text-align: center;
  margin-bottom: 20px;
  animation: fadeIn 1s ease-out;
}

/* Animation for fadeIn effect */
@keyframes fadeIn {
  0% {
    opacity: 0;
    transform: translateY(-10px);
  }
  100% {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Button container styling */
.buttons-container {
  display: flex;
  justify-content: center;
  gap: 15px;
}

/* Common styling for export buttons */
.export-button {
  font-size: 16px;
  padding: 12px 24px;
  border: none;
  border-radius: 10px;
  cursor: pointer;
  transition: transform 0.3s ease, background-color 0.3s ease;
  font-weight: bold;
  text-transform: uppercase;
}

/* PDF button styling */
.pdf-button {
  background-color: #3498db;
  color: white;
}

.pdf-button:hover {
  background-color: #2980b9;
  transform: scale(1.05);
}

/* CSV button styling */
.csv-button {
  background-color: #2ecc71;
  color: white;
}

.csv-button:hover {
  background-color: #27ae60;
  transform: scale(1.05);
}

/* Styling for hover and click effects */
.export-button:active {
  transform: scale(0.98);
}
</style>
