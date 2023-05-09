// next.config.js
/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  swcMinify: true,
  async rewrites() {
    return [
      {
        source: "/api/chat",
        destination: "http://localhost:5000/agents",
      },
    ];
  },
};

module.exports = nextConfig;
