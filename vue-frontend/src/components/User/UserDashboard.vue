<template>
  <header>
    <div class="user-dashboard-header">
      <h1>Welcome to PulseBI Dashboard</h1>
      <button @click="goToAlertsPanel">Alerts Panel</button>
      <button @click="goToUserSettings">User Settings</button>
    </div>
    <nav class="sidebar">
      <ul>
        <li><a href="/user-dashboard">Dashboard</a></li>
        <li><a href="/trend-analytics">Analytics</a></li>
        <li><a href="/user-settings">Settings</a></li>
        <li><a href="/alerts-panel">Notification</a></li>
      </ul>
    </nav>
  </header>

  <main class="user-dashboard-content">
    <section class="kpi-section">
      <h2>Key Performance Indicators (KPIs)</h2>
      <div class="kpi-card">
        <p>Total Sales</p>
        <p>{{ totalSales }}</p>
      </div>
      <div class="kpi-card">
        <p>Active Customers</p>
        <p>{{ activeCustomers }}</p>
      </div>
      <div class="kpi-card">
        <p>Revenue Forecasted</p>
        <p>{{ revenueForecast }}</p>
      </div>
    </section>

    <section class="analytics-section">
      <h2>Sales Overtime $ (USD)</h2>
      <canvas id="salesTrendChart"></canvas>  
    </section>

    <section class="notifications-section">
      <h2>Top Products</h2>
      <ul>
        <li v-for="product in topProducts" :key="product.product_name">
          {{ product.product_name }} - {{ product.sales }}
        </li>
      </ul>
    </section>
    
    <section class="active-users-section">
      <h2>Customer Last 4 Hours Activity</h2>
    </section>
  </main>

  <footer class="user-dashboard-footer">
    <p>&copy; 2023 PulseBI. All rights reserved.</p>
  </footer>
</template>




<script setup>

import { ref, onMounted, watchEffect } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';
import { useHead } from '@vueuse/head';
import { Chart, CategoryScale, LinearScale, LineElement, PointElement, Title, Tooltip, Legend, LineController } from 'chart.js';

// Register all necessary components, including the LineController
Chart.register(CategoryScale, LinearScale, LineElement, PointElement, Title, Tooltip, Legend, LineController);

const router = useRouter();

const goToAlertsPanel = () => {
  router.push('/alerts-panel');
};

const goToUserSettings = () => {
  router.push('/user-settings');
};

// Reactive states
const totalSales = ref(0);
const activeCustomers = ref(0);
const revenueForecast = ref(0);
const topProducts = ref([]);

const salesTrend = ref([]); // For the sales trend chart

// Fetch all dashboard data
const fetchDashboardData = async () => {
  try {
    const response = await axios.get('http://127.0.0.1:5000/api/user_dashboard_data');
    const sale_response = await axios.get('http://127.0.0.1:5000/prediction/predicted-nextweek-sales-Trend-api');
    const sales_data = sale_response.data.predicted_sales_next_week;

    const data = response.data.dashboard_data;

    totalSales.value = data['Total sales'];
    activeCustomers.value = data['Active Customers'];
    revenueForecast.value = data['Revenue Forecasted'];
    topProducts.value = data['Top Products'] || [];

    salesTrend.value = sales_data; // Set the sales trend data
  } catch (error) {
    if (error.response) {
      console.error('Error fetching dashboard data:', error.response.data);
      if (error.response.status === 401) {
        console.error("Unauthorized. Please log in again.");
      }
    } else {
      console.error("Error:", error.message);
    }
  }
};

const renderSalesTrendChart = () => {
  if (!salesTrend.value.length) return; // Prevent rendering if data is empty

  const ctx = document.getElementById('salesTrendChart').getContext('2d');

  new Chart(ctx, {
    type: 'line',  // Use 'line' for the line chart
    data: {
      labels: ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5', 'Day 6', 'Day 7'],  
      datasets: [{
        label: 'Predicted Sales for Next Week',
        data: salesTrend.value,  // Use salesTrend reactive data
        borderColor: 'rgba(75, 192, 192, 1)',
        backgroundColor: 'rgba(75, 192, 192, 0.2)',
        fill: true,
        tension: 0.1,
      }]
    },
    options: {
      responsive: true,
      scales: {
        y: {
          beginAtZero: false,
        },
      },
    }
  });
};

// Lifecycle hook
onMounted(() => {
  fetchDashboardData();
});

// Watch the salesTrend data and render chart when updated
watchEffect(() => {
  if (salesTrend.value.length > 0) {
    renderSalesTrendChart();
  }
});

useHead({
  title: 'PulseBI - Real-Time Data Analytics Dashboard',
  meta: [
    { name: 'description', content: 'Unlock the power of real-time data analytics with PulseBI. Visualize, analyze, and make smarter business decisions with our intuitive dashboard.' },
    { name: 'viewport', content: 'width=device-width, initial-scale=1.0' },
    { name: 'author', content: 'Timothy Mbata' },
    { name: 'keywords', content: 'data analytics, real-time analytics, business intelligence, PulseBI, dashboards, AI insights, Timothy Mbata' },
    { name: 'robots', content: 'index, follow' },
    { property: 'og:title', content: 'PulseBI - Real-Time Analytics for Smarter Business Decisions' },
    { property: 'og:description', content: 'Transform your business with real-time data insights and smart dashboards from PulseBI.' },
    { property: 'og:image', content: '/images/pulsebi-logo.png' },
    { property: 'og:url', content: 'http://localhost:8080/landing-page' },
    { property: 'og:type', content: 'website' },
    { name: 'twitter:card', content: 'summary_large_image' },
    { name: 'twitter:title', content: 'PulseBI Dashboard' },
    { name: 'twitter:description', content: 'Real-time analytics and AI-powered dashboards for your business.' },
    { name: 'twitter:image', content: '/images/pulsebi-logo.png' }
  ]
});


</script>


<style scoped>
/* User Dashboard Header */
.user-dashboard-header {
  background: #ffffff;
  padding: 1.5rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
  color: #111827;

  h1 {
    font-size: 1.75rem;
    font-weight: bold;
    color: #1f2937;
  }

  button {
    background-color: #3b82f6;
    color: #fff;
    border: none;
    padding: 0.75rem 1.25rem;
    border-radius: 8px;
    cursor: pointer;
    transition: transform 0.3s ease, background-color 0.3s;

    &:hover {
      transform: scale(1.05);
      background-color: #2563eb;
    }
  }
}

/* Sidebar Styling */
.sidebar {
  width: 240px;
  background-color: #1f2937;
  color: #fff;
  padding: 1.25rem;
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  margin-top: 80px;
  animation: slideIn 0.5s ease-out;

  ul {
    list-style: none;
    padding: 0;

    li {
      margin: 1.5rem 0;

      a {
        color: #cbd5e1;
        text-decoration: none;
        font-weight: 500;
        font-size: 1rem;
        display: block;
        padding: 0.5rem 0;
        transition: color 0.3s ease, padding-left 0.3s;

        &:hover {
          color: #ffffff;
          padding-left: 1rem;
        }
      }
    }
  }
}

/* Main Content Styling */
.user-dashboard-content {
  margin-left: 260px;
  padding: 2rem;
  background-color: #f4f6f9;
  min-height: 100vh;
  animation: fadeInContent 0.6s ease-out;

  section {
    margin-bottom: 2rem;

    h2 {
      font-size: 1.5rem;
      color: #111827;
      margin-bottom: 1rem;
      font-weight: 600;
    }
  }

  /* Key Performance Indicator Cards */
  .kpi-section {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 1.5rem;

    .kpi-card {
      background: #ffffff;
      padding: 1.5rem;
      border-radius: 12px;
      box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
      font-weight: 600;
      text-align: center;
      color: #3b82f6;
      transition: transform 0.3s ease, box-shadow 0.3s ease;
      animation: fadeInScale 0.6s ease;

      &:hover {
        transform: scale(1.05);
        box-shadow: 0 6px 15px rgba(0, 0, 0, 0.1);
      }
    }
  }

  /* Sections for Analytics, Notifications, etc. */
  .notifications-section, .active-users-section {
    background: #ffffff;
    padding: 1.5rem;
    border-radius: 12px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
    transition: transform 0.3s ease;
    animation: fadeInSection 0.7s ease-out;

    &:hover {
      transform: translateY(-5px);
    }
  }
}
.analytics-section {
  background: #ffffff;
  padding: 1.5rem;
  border-radius: 12px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
  animation: fadeInSection 0.7s ease-out;

  canvas {
    width: 100% !important;
    height: auto !important;
    max-width: 100%;
    margin-top: 1rem;
  }
}

/* Footer Styling */
.user-dashboard-footer {
  text-align: center;
  padding: 1.5rem;
  background: #ffffff;
  box-shadow: 0 -2px 10px rgba(0, 0, 0, 0.05);
  color: #6b7280;
  font-size: 0.9rem;
}

/* Mobile Adjustments */
@media (max-width: 768px) {
  /* Sidebar */
  .sidebar {
    width: 100%;
    position: relative;
    margin-top: 0;
    box-shadow: none;
    animation: none;
  }

  /* Main Content */
  .user-dashboard-content {
    margin-left: 0;
    padding: 1rem;
  }

  /* KPI Cards */
  .kpi-section {
    grid-template-columns: 1fr 1fr; /* Two cards per row on mobile */
  }

  /* Header */
  .user-dashboard-header {
    flex-direction: column;
    align-items: flex-start;

    button {
      width: 100%;
      margin-top: 1rem;
    }
  }

  /* Sidebar Links */
  .sidebar ul li a {
    font-size: 0.9rem;
  }
}

/* Animations */
@keyframes fadeInScale {
  from {
    opacity: 0;
    transform: scale(0.95);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}

@keyframes slideIn {
  from {
    transform: translateX(-100%);
  }
  to {
    transform: translateX(0);
  }
}

@keyframes fadeInContent {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

@keyframes fadeInSection {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>