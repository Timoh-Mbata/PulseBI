<template>
  <div class="container">
    <!-- Sidebar -->
    <aside class="sidebar">
      <h2>PulseBI Admin</h2>
      <nav>
        <ul>
          <li><router-link to="/admin/dashboard">Dashboard</router-link></li>
          <li><router-link to="/admin/users">Users</router-link></li>
          <li><router-link to="/admin/data-sources">Data Sources</router-link></li>
          <li><router-link to="/admin/Metrics">Metrics</router-link></li>
          <li><router-link to="/admin/predictions">Predictions</router-link></li>
          <li><router-link to="/admin/alerts">Alerts</router-link></li>
        </ul>
      </nav>
    </aside>

    <!-- Main content -->
    <main class="main-content">
      <header class="header">
        <h2>Welcome {{ username }} to PulseBI Admin Dashboard</h2>
      </header>

      <section class="cards">
        <div class="card">
          <h3>Active Users</h3>
          <p>{{ activeUsers }}</p>
        </div>
        <div class="card">
          <h3>Active Data Sources</h3>
          <p>{{ activeDataSources }}</p>
        </div>
        <div class="card">
          <h3>Live Data Updates</h3>
          <p>{{ isliveData }}</p>
        </div>
        <div class="card full-width">
          <h3>Accuracy Rate Graph of Predictions</h3>
          <p>{{ activePredictions }}</p>
        </div>
      </section>

      <section class="alerts">
        <h3>Recent Alerts</h3>
        <table>
          <thead>
            <tr>
              <th>Time</th>
              <th>Condition</th>
              <th>Metric</th>
              <th>Status</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(alert, index) in recentAlerts" :key="index">
              <td>{{ alert.time }}</td>
              <td>{{ alert.condition }}</td>
              <td>{{ alert.metric }}</td>
              <td>{{ alert.status }}</td>
            </tr>
          </tbody>
        </table>
      </section>
    </main>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: "AdminDashboard",
  data() {
    return {
      username: "",  // Will be updated with the API response
      activeUsers: 102,
      activeDataSources: 17,
      isliveData: "Yes",
      activePredictions: "92% Accuracy",
      recentAlerts: [
        { time: "12:00", condition: "High CPU", metric: "Server Load", status: "Critical" },
        { time: "14:30", condition: "Memory Spike", metric: "Memory Usage", status: "Warning" },
        // Add more mock alerts as needed
      ]
    };
  },
  created() {
    this.fetchUser();
  },
  methods: {
    async fetchUser() {
      try {
        const response = await axios.get('http://127.0.0.1:5000/me', {
          headers: {
            Authorization: `Bearer ${localStorage.getItem('jwtToken')}`
          }
        });

        console.log(response.data);  // Log response for debugging
        this.username = response.data.username;  // Store the username from the backend
      } catch (error) {
        console.error("Error fetching user:", error);
      }
    }
  }
};
</script>


<style scoped>
.container {
  display: flex;
  min-height: 100vh;
  font-family: Arial, sans-serif;
}

/* Sidebar styling */
.sidebar {
  width: 220px;
  background-color: #2c3e50;
  color: #fff;
  padding: 20px;
}

.sidebar h2 {
  font-size: 20px;
  margin-bottom: 20px;
}

.sidebar ul {
  list-style: none;
  padding: 0;
}

.sidebar li {
  margin-bottom: 12px;
}

.sidebar a {
  color: #ecf0f1;
  text-decoration: none;
}

.sidebar a:hover {
  text-decoration: underline;
}

/* Main content styling */
.main-content {
  flex: 1;
  padding: 30px;
  background-color: #f4f4f4;
}

.header {
  margin-bottom: 30px;
}

.cards {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  margin-bottom: 40px;
}

.card {
  background-color: white;
  border-radius: 6px;
  padding: 20px;
  box-shadow: 0 0 8px rgba(0,0,0,0.1);
  flex: 1 1 200px;
}

.full-width {
  flex: 1 1 100%;
}

.alerts h3 {
  margin-bottom: 10px;
}

table {
  width: 100%;
  border-collapse: collapse;
  background-color: white;
  box-shadow: 0 0 8px rgba(0,0,0,0.1);
}

th, td {
  padding: 10px 15px;
  border: 1px solid #ccc;
  text-align: left;
}

thead {
  background-color: #e0e0e0;
}
/* Animations */
@keyframes fadeInUp {
  0% {
    opacity: 0;
    transform: translateY(20px);
  }
  100% {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Animate main content when page loads */
.main-content {
  animation: fadeInUp 0.8s ease-in-out;
}

/* Card appearance animation */
.card {
  animation: fadeInUp 0.8s ease forwards;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

/* Card hover effect */
.card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 20px rgba(0,0,0,0.15);
}

/* Sidebar link hover glow */
.sidebar a {
  position: relative;
  transition: color 0.3s ease;
}

.sidebar a::after {
  content: '';
  position: absolute;
  left: 0;
  bottom: -2px;
  width: 0%;
  height: 2px;
  background-color: #1abc9c;
  transition: width 0.3s ease;
}

.sidebar a:hover::after {
  width: 100%;
}

.sidebar a:hover {
  color: #1abc9c;
}

/* Table row hover effect */
table tbody tr {
  transition: background-color 0.3s ease;
}

table tbody tr:hover {
  background-color: #f1f1f1;
}

</style>
