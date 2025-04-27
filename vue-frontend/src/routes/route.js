import { createRouter, createWebHistory } from 'vue-router';
import UserDashboard from '@/components/User/UserDashboard.vue';
import AiPredictions from '@/components/dashboard/AiPredictions.vue';
import AlertsPanel from '@/components/dashboard/AlertsPanel.vue';   
import UserSettings from '@/components/dashboard/UserSettings.vue';
import DataSources from '@/components/dashboard/DataSources.vue';
import KpiSummary from '@/components/dashboard/KpiSummary.vue';
import LiveData from '@/components/dashboard/LiveData.vue';
import ReportsAndExports from '@/components/dashboard/ReportsAndExports.vue';
import TrendAnalytics from '@/components/dashboard/TrendAnalytics.vue';
import AdminDashboard from '@/components/Admin/Admin/AdminDashboard.vue';
import SignUp from '@/components/User/SignUp.vue';
import loginPage from '@/components/User/loginPage.vue';
import LandingPage from '@/landingPage.vue';
import ContactUs  from '@/components/dashboard/ContactUs.vue';
const routes = [
  {
    path: '/user-dashboard',
    name: 'UserDashboard',
    component: UserDashboard,
    meta: { requiresAuth: true, role: 'user' }
  },
  {
    path: '/landing-page',
    name: 'LandingPage',
    component: LandingPage,
  },
  {
    path: '/ai-predictions',
    name: 'AiPredictions',
    component: AiPredictions,
  },
  {
    path: '/sign-up',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/login',
    name: 'Login',
    component: loginPage
  },
  {
    path:'/contact-us',
    name:'ContactUs',
    component: ContactUs
  },
  {
    path: '/alerts-panel',
    name: 'AlertsPanel',
    component: AlertsPanel,

  },
  {
    path: '/user-settings',
    name: 'UserSettings',
    component: UserSettings,
  },
  {
    path: '/admin/data-sources',
    name: 'DataSources',
    component: DataSources,
  },
  {
    path: '/kpi-summary',
    name: 'KpiSummary',
    component: KpiSummary,
  },
  {
    path: '/admin/live-data',
    name: 'LiveData',
    component: LiveData,
  },
  {
    path: '/reports-and-exports',
    name: 'ReportsAndExports',
    component: ReportsAndExports,
  },
  {
    path: '/admin-dashboard',
    name: 'AdminDashboard',
    component: AdminDashboard,
  },
  {
    path: '/trend-analytics',
    name: 'TrendAnalytics',
    component: TrendAnalytics,
  },
  {
    path: '/',
    redirect: '/landing-page'
  }
];


const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
