<template>
  <div class="landing-page">
    <!-- HEADER -->
    <header class="header">
      <div class="container">
        <h1 class="logo">PulseBI</h1>
        <button class="hamburger" @click="toggleNav">&#9776;</button>
        <nav :class="['nav', { open: navOpen }]">
          <ul>
            <li><a href="#features" class="btn primary-btn">Features</a></li>
            <li><a href="#pricing" class="btn primary-btn">Pricing</a></li>
            <li><a href="/contact-us" class="btn primary-btn">Contact</a></li>
            <li><a href="/login" class="btn primary-btn">Login</a></li>
            <li><a href="/sign-up" class="btn primary-btn">Sign Up</a></li>
          </ul>
        </nav>
      </div>
    </header>

    <!-- HERO SECTION -->
    <section class="hero reveal">
      <div class="hero-overlay">
        <div class="hero-content">
          <div class="text">
            <h2>Unlock the Power of Data with PulseBI</h2>
            <p class="subtitle">Real-time analytics. AI insights. Better decisions.</p>
            <a href="/sign-up" class="btn primary-btn">Start Free Trial</a>
          </div>
        </div>
      </div>
    </section>

    <!-- FEATURES -->
    <section id="features" class="section features">
      <div class="container">
        <h2 class="section-title">Key Features</h2>
        <div class="cards">
          <div class="card reveal">
            <img src="/tracker.jpg" alt="Tracker" />
            <h3>Real-Time Tracking</h3>
            <p>Monitor metrics live, act instantly.</p>
          </div>
          <div class="card reveal">
            <img src="/feature2.jpg" alt="AI Insights" />
            <h3>AI Insights</h3>
            <p>Smarter predictions with ML intelligence.</p>
          </div>
          <div class="card reveal">
            <img src="/feature 3.jpg" alt="Custom Dashboards" />
            <h3>Custom Dashboards</h3>
            <p>Tailor views to match your business goals.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- PRICING -->
    <section id="pricing" class="pricing reveal">
      <div class="container">
        <h2>Pricing Plans</h2>
        <div class="pricing-cards">
          <div class="pricing-card">
            <h3>Basic</h3>
            <p>$19/mo</p>
            <ul>
              <li>5 Data Sources</li>
              <li>Basic Analytics</li>
              <li>Email Support</li>
            </ul>
            <a href="/sign-up" class="btn">Sign Up</a>
          </div>
          <div class="pricing-card popular">
            <h3>Pro</h3>
            <p>$49/mo</p>
            <ul>
              <li>20 Data Sources</li>
              <li>Advanced Analytics</li>
              <li>Priority Support</li>
            </ul>
            <a href="/sign-up" class="btn">Get Started</a>
          </div>
          <div class="pricing-card">
            <h3>Enterprise</h3>
            <p>Custom</p>
            <ul>
              <li>Unlimited Data Sources</li>
              <li>Custom Analytics</li>
              <li>Dedicated Manager</li>
            </ul>
            <a href="/contact-us" class="btn">Contact Us</a>
          </div>
        </div>
      </div>
    </section>

    <!-- BACK TO TOP -->
    <button class="back-to-top" @click="scrollToTop">↑</button>

    <!-- FOOTER -->
    <footer class="footer">
      <div class="container">
        <p>© 2025 PulseBI | Your Partner in Data Excellence</p>
      </div>
    </footer>
  </div>
</template>

<script>
import { useHead } from '@vueuse/head'
import { onMounted, ref } from 'vue'

export default {
  name: 'LandingPage',
  setup() {
    const navOpen = ref(false)

    // SEO Meta Tags
    useHead({
      title: 'PulseBI - Unlock the Power of Data',
      meta: [
        { name: 'description', content: 'Unlock the power of real-time data analytics with PulseBI for smarter business decisions.' },
        { name: 'author', content: 'Timothy Mbata' },
        { name: 'keywords', content: 'data analytics, real-time insights, business intelligence, PulseBI, Timothy Mbata' },
        { name: 'robots', content: 'index, follow' },
        { property: 'og:title', content: 'PulseBI - Unlock the Power of Data' },
        { property: 'og:description', content: 'Real-time data analytics and AI insights for businesses.' },
        { property: 'og:image', content: '/images/pulsebi-logo.png' },
        { property: 'og:url', content: 'https://yourwebsite.com' }
      ]
    })

    // Nav toggle
    const toggleNav = () => {
      navOpen.value = !navOpen.value
    }

    // Scroll to top
    const scrollToTop = () => {
      window.scrollTo({ top: 0, behavior: 'smooth' })
    }

    // Reveal animation on scroll
    onMounted(() => {
      const observer = new IntersectionObserver(
        (entries) => {
          entries.forEach((entry) => {
            if (entry.isIntersecting) {
              entry.target.classList.add('visible')
            }
          })
        },
        { threshold: 0.1 }
      )

      document.querySelectorAll('.reveal').forEach((el) => observer.observe(el))
    })

    return {
      navOpen,
      toggleNav,
      scrollToTop
    }
  }
}
</script>



<style scoped>
/* GLOBAL */
.landing-page {
  font-family: 'Segoe UI', sans-serif;
  color: #333;
  line-height: 1.6;
  background: #f7f9fc;
  overflow-x: hidden;
}

.container {
  max-width: 1100px;
  margin: auto;
  padding: 0 20px;
}

/* HEADER */
.header {
  background: #1c1f26;
  padding: 15px 0;
  color: #fff;
}

.logo {
  font-size: 28px;
  font-weight: bold;
}

.hamburger {
  font-size: 26px;
  background: none;
  border: none;
  color: white;
  cursor: pointer;
  display: none;
}

.nav ul {
  display: flex;
  gap: 20px;
}

.nav.open ul {
  flex-direction: column;
}

/* HERO */
.hero {
  position: relative;
  height: 70vh;
  background: url('/public/image-to-use.png') no-repeat center center/cover;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 30px 0;
  scroll-behavior: smooth;
  transform: translateZ(0);
  will-change: transform;
  transition: transform 0.3s ease;
}

.hero-overlay {
  position: relative;
  z-index: 2;
  text-align: center;
  color: white;
  animation: floatIn 2s ease-out;
  background: rgba(0, 0, 0, 0.5);
  padding: 40px;
  border-radius: 20px;
}

.hero-content .text h2 {
  font-size: 2.5rem;
  margin-bottom: 20px;
}

.hero-content .text .subtitle {
  font-size: 1.2rem;
  margin-bottom: 20px;
}

@keyframes floatIn {
  from {
    opacity: 0;
    transform: translateY(40px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* FEATURES */
.features .cards {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}

.card {
  background: #fff;
  border-radius: 16px;
  padding: 20px;
  flex: 1;
  text-align: center;
  box-shadow: 0 2px 10px rgba(0,0,0,0.1);
  transition: transform 0.3s;
}

.card:hover {
  transform: translateY(-5px);
  box-shadow: 0 4px 20px rgba(0,0,0,0.2);
  transform: scale(1.05);
}

.card img {
  width: 100%;
  max-height: 200px;
  object-fit: cover;
  border-radius: 8px;
  margin-bottom: 10px;
}

/* PRICING */
.pricing-cards {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}

.pricing-card {
  background: #fff;
  border-radius: 16px;
  padding: 20px;
  flex: 1;
  min-width: 250px;
  text-align: center;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

.pricing-card.popular {
  border: 2px solid #28a745;
}

.pricing-card ul {
  list-style: none;
  padding: 0;
}

/* FOOTER */
.footer {
  background: #1c1f26;
  color: white;
  text-align: center;
  padding: 20px;
}

/* BUTTONS */
.btn {
  display: inline-block;
  background: #007bff;
  color: white;
  padding: 10px 20px;
  border-radius: 8px;
  text-decoration: none;
  transition: background 0.3s;
}

.btn:hover {
  background: #0056b3;
}

.primary-btn {
  background: #28a745;
}

.primary-btn:hover {
  background: #1c7c33;
}

/* ANIMATIONS */
.reveal {
  opacity: 0;
  transform: translateY(20px);
  transition: all 0.7s ease;
}

.reveal.visible {
  opacity: 1;
  transform: translateY(0);
}

/* BACK TO TOP */
.back-to-top {
  position: fixed;
  bottom: 30px;
  right: 30px;
  background: #28a745;
  color: white;
  border: none;
  border-radius: 50%;
  font-size: 22px;
  width: 45px;
  height: 45px;
  cursor: pointer;
  box-shadow: 0 2px 10px rgba(0,0,0,0.2);
  transition: background 0.3s ease;
}

.back-to-top:hover {
  background: #1c7c33;
}

/* RESPONSIVE */
@media (max-width: 768px) {
  .nav ul {
    flex-direction: column;
  }
  .hamburger {
    display: block;
  }
  .features .cards,
  .pricing-cards {
    flex-direction: column;
  }
  .hero-content .text h2 {
    font-size: 1.8rem;
  }
}
</style>
