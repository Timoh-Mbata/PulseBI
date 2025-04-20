<template>
  <!--This is the user Dashboard being designed it has KPIs,a sidebar-fro easy navigation and a -->
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
        <li><a href="/user-settings">settings</a></li>
        <li><a href="/alerts-panel">Notification</a></li>
      </ul>
    </nav>
  </header>
  <main class="user-dashboard-content">
    <section class="kpi-section">
      <h2>Key Performance Indicators (KPIs)</h2>
      <div class="kpi-card">Total Sales</div>
      <div class="kpi-card">Inventory left</div>
      <div class="kpi-card">active Users</div>
      <div class="kpi-card">Revenue Forecasted</div>
    </section>
    <section class="analytics-section">
      <h2>Sales Overtime</h2>
      <!-- Add your analytics charts or components here -->
    </section>

    <section class="notifications-section">
      <h2>Top Products</h2>
      <!-- Table of Top 5 selling products here -->
    </section>

    <section class="active-users-section">
      <h2>Active Users</h2>
      <!-- Graphs of active users against last 4 hours  -->
    </section>
  </main>
  <footer class="user-dashboard-footer">
    <p>&copy; 2023 PulseBI. All rights reserved.</p>
  </footer>

</template>

<script setup>
import { useHead } from '@vueuse/head'
import { useRouter } from 'vue-router'

const router = useRouter()

const goToAlertsPanel = () => {
  router.push('/alerts-panel')
}

const goToUserSettings = () => {
  router.push('/user-settings')
}

useHead({
  title: 'PulseBI - Real-Time Data Analytics Dashboard',
  meta: [
    { name: 'description', content: 'Unlock the power of real-time data analytics with PulseBI. Visualize, analyze, and make smarter business decisions with our intuitive dashboard.' },
    { name: 'viewport', content: 'width=device-width, initial-scale=1.0' },
    { name: 'author', content: 'Timothy Mbata' },
    { name: 'keywords', content: 'data analytics, real-time analytics, business intelligence, PulseBI, dashboards, AI insights, Timothy Mbata' },
    { name: 'robots', content: 'index, follow' },

    // Open Graph
    { property: 'og:title', content: 'PulseBI - Real-Time Analytics for Smarter Business Decisions' },
    { property: 'og:description', content: 'Transform your business with real-time data insights and smart dashboards from PulseBI.' },
    { property: 'og:image', content: '/images/pulsebi-logo.png' },
    { property: 'og:url', content: 'https://yourwebsite.com/user-dashboard' },
    { property: 'og:type', content: 'website' },

    // Twitter
    { name: 'twitter:card', content: 'summary_large_image' },
    { name: 'twitter:title', content: 'PulseBI Dashboard' },
    { name: 'twitter:description', content: 'Real-time analytics and AI-powered dashboards for your business.' },
    { name: 'twitter:image', content: '/images/pulsebi-logo.png' }
  ]
})
</script>
<style scoped lang="scss">
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
  .analytics-section, .notifications-section, .active-users-section {
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

/* Footer Styling */
.user-dashboard-footer {
  text-align: center;
  padding: 1.5rem;
  background: #ffffff;
  box-shadow: 0 -2px 10px rgba(0, 0, 0, 0.05);
  color: #6b7280;
  font-size: 0.9rem;
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