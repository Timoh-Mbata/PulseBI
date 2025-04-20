<template>
  <div class="admin-dashboard">
    <!-- Header -->
    <header class="dashboard-header">
      <h1>PulseBI Admin Dashboard</h1>
      <div class="profile-info">
        <img src="https://via.placeholder.com/50" alt="Admin" class="profile-pic" />
        <span>Welcome, Admin</span>
      </div>
    </header>

    <!-- Overview Cards -->
    <section class="overview-section">
      <div class="card">Total Users: 120</div>
      <div class="card">Reports Generated: 58</div>
      <div class="card">Active Sources: 12</div>
      <div class="card">Predictions Made: 340</div>
    </section>

    <!-- Sections -->
    <section class="panel"><h2>User Management</h2><p>View, edit, and manage user accounts.</p></section>
    <section class="panel"><h2>System Overview</h2><p>Monitor platform stats and server status.</p></section>
    <section class="panel"><h2>Analytics Monitoring</h2><p>Track dashboard and model usage.</p></section>
    <section class="panel"><h2>Data Sources</h2><p>Manage your connected databases and APIs.</p></section>
    <section class="panel"><h2>Report Downloads</h2><p>Access export history and download logs.</p></section>
    <section class="panel"><h2>AI & Predictions</h2><p>Manage models and prediction logs.</p></section>
    <section class="panel"><h2>Tasks & Notifications</h2><p>Admin alerts and pending tasks.</p></section>
    <section class="panel"><h2>System Settings</h2><p>Platform preferences, API keys, and more.</p></section>
  </div>
</template>

<script>
export default {
  name: 'AdminDashboard',
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

.admin-dashboard {
  font-family: 'Inter', sans-serif;
  background-color: #121212;
  color: #f0f0f0;
  max-width: 1200px;
  margin: 0 auto;
  padding: 1rem;
}

.dashboard-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  padding: 1.5rem;
  border-radius: 12px;
  background-color: #1e1e1e;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.6);
  margin-bottom: 2rem;
}

.dashboard-header h1 {
  font-size: clamp(1.5rem, 2.5vw, 2rem);
  font-weight: 700;
  color: #ffffff;
  margin: 0;
}

.profile-info {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  margin-top: 1rem;
}

.profile-pic {
  border-radius: 50%;
  width: 50px;
  height: 50px;
  border: 2px solid #00bcd4;
}

.profile-info span {
  font-weight: 600;
  color: #cccccc;
  font-size: 1rem;
}

.overview-section {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 1rem;
  margin-bottom: 2.5rem;
}

.card {
  background-color: #2a2a2a;
  padding: 1.5rem;
  border-radius: 10px;
  text-align: center;
  font-weight: bold;
  font-size: 1.2rem;
  color: #00bcd4;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.4);
  transition: transform 0.3s ease;
}

.card:hover {
  transform: translateY(-5px);
}

.panel {
  background-color: #1e1e1e;
  border: 1px solid #333;
  padding: 1.25rem;
  margin-bottom: 1.5rem;
  border-radius: 10px;
  box-shadow: 0 3px 8px rgba(255, 64, 129, 0.2);
  transition: box-shadow 0.3s ease;
}

.panel:hover {
  box-shadow: 0 6px 14px rgba(255, 64, 129, 0.3);
}

.panel h2 {
  margin-bottom: 0.5rem;
  font-size: clamp(1.1rem, 2vw, 1.3rem);
  color: #ffffff;
}

.panel p {
  color: #cccccc;
  font-size: 0.95rem;
  line-height: 1.5;
}

@media (max-width: 768px) {
  .dashboard-header {
    flex-direction: column;
    align-items: flex-start;
    padding: 1rem;
  }

  .profile-info {
    margin-top: 0.5rem;
  }

  .card {
    font-size: 1rem;
    padding: 1.2rem;
  }

  .panel {
    padding: 1rem;
  }

  .panel h2 {
    font-size: 1.1rem;
  }
}
</style>
