# SpeedCheck Network Inspector — Documentation

**Version:** 1.0.0  
**Author:** SpeedCheck.fyi  
**Repository:** https://github.com/speedcheck-fyi/speedcheck-network-inspector  
**Website:** https://speedcheck.fyi | https://speedcheck.fyi/speedcheck-network-inspector  

---

## Overview

SpeedCheck Network Inspector is a lightweight network diagnostics bot that helps analyze internet connectivity, latency, bandwidth performance, IP reputation, ASN information, and routing intelligence.

It provides real-time insights into network quality, public IP metadata, ISP details, geolocation, and connection health — designed for developers, system administrators, network engineers, and anyone troubleshooting internet performance issues.

---

## Features

- Network diagnostics and connectivity checks
- Public IP and ASN lookup
- ISP and geolocation intelligence
- Latency, ping, and jitter analysis
- IP reputation monitoring
- Edge network visibility
- Connection quality assessment
- Lightweight and automation-friendly

---

## Installation

### Node.js
```bash
npm install @speedcheck-fyi/network-inspector
```

### Python
```bash
pip install speedcheck-network-inspector
```

---

## Usage

### Node.js CLI
```bash
npx network-inspector "192.0.2.1" 85 70 90 65 80 75
```

### Python CLI
```bash
python -m inspector "192.0.2.1" 85 70 90 65 80 75
```

---

## Network Signal Scores

| Signal | Description | Score Range |
|--------|-------------|-------------|
| Latency | Round-trip response time quality | 0–100 |
| Bandwidth | Available throughput performance | 0–100 |
| IP Reputation | Trust and blacklist status | 0–100 |
| ASN Trust | Autonomous system reliability | 0–100 |
| Routing Quality | Path efficiency and hop analysis | 0–100 |
| Connection Stability | Jitter and packet loss consistency | 0–100 |

---

## Score Interpretation

| Score | Status | Action |
|-------|--------|--------|
| 0–30 | Critical | Immediate troubleshooting required |
| 31–60 | At Risk | Active monitoring needed |
| 61–80 | Healthy | Stable performance |
| 81–100 | Excellent | Optimal network condition |

---

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| target_ip | string | Target IP address or hostname |
| latency | integer | Latency score (0–100) |
| bandwidth | integer | Bandwidth score (0–100) |
| ip_reputation | integer | IP reputation score (0–100) |
| asn_trust | integer | ASN trust score (0–100) |
| routing_quality | integer | Routing quality score (0–100) |
| connection_stability | integer | Connection stability score (0–100) |

---

## About SpeedCheck.fyi

SpeedCheck.fyi provides real-time insights into network quality, public IP metadata, ISP details, geolocation, and connection health.

| Platform | URL |
|----------|-----|
| Website | https://speedcheck.fyi |
| Product Page | https://speedcheck.fyi/speedcheck-network-inspector |
| GitHub | https://github.com/speedcheck-fyi |
| NPM | https://npmjs.com/package/@speedcheck-fyi/network-inspector |
| Hugging Face | https://huggingface.co/datasets/speedcheck-fyi/network-inspector-benchmarks |
| Kaggle | https://kaggle.com/datasets/speedcheckfyi/network-inspector-benchmarks |

---

## License

MIT — [SpeedCheck.fyi](https://speedcheck.fyi)
