# SpeedCheck Network Inspector 🌐⚡

[![npm](https://img.shields.io/npm/v/@speedcheck-fyi/network-inspector)](https://npmjs.com/package/@speedcheck-fyi/network-inspector)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20797019.svg)](https://doi.org/10.5281/zenodo.20797019)

A lightweight network diagnostics bot that helps analyze internet connectivity, latency, bandwidth performance, IP reputation, ASN information, and routing intelligence. Powered by [SpeedCheck.fyi](https://speedcheck.fyi).

## Features

- Network Diagnostics — comprehensive connectivity checks
- Public IP & ASN Lookup — identifies IP metadata and autonomous system info
- ISP & Geolocation Intelligence — pinpoint internet service provider and location
- Latency, Ping & Jitter Analysis — measures connection responsiveness
- IP Reputation Monitoring — tracks IP trust and blacklist status
- Edge Network Visibility — insight into CDN and edge routing
- Connection Quality Assessment — overall network health score
- Lightweight and automation-friendly — easy CI/CD integration
- CLI support in Node.js and Python
- Benchmark dataset included (20 network diagnostic cases)

## Quick Start

### Node.js

```bash
npm install @speedcheck-fyi/network-inspector
npx network-inspector "192.0.2.1" 85 70 90 65 80 75
```

### Python

```bash
pip install speedcheck-network-inspector
python -m inspector "192.0.2.1" 85 70 90 65 80 75
```

## Output

```
Target IP: 192.0.2.1
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Latency Score:               85 / 100  [Excellent]
Bandwidth Score:             70 / 100  [Healthy]
IP Reputation Score:         90 / 100  [Excellent]
ASN Trust Score:              65 / 100  [Healthy]
Routing Quality Score:        80 / 100  [Healthy]
Connection Stability Score:   75 / 100  [Healthy]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Overall Network Health:      78 / 100
Priority Signal:             ASN Trust (lowest — act first)

Network Info:
  ISP:                  Example Networks Inc
  ASN:                  AS64512
  Geolocation:          United States
  Connection Type:      Fiber
```

## Project Structure

```
speedcheck-network-inspector/
├── index.ts              # TypeScript inspector
├── inspector.py          # Python inspector
├── package.json          # NPM package config
├── package-lock.json     # NPM lock file
├── tsconfig.json         # TypeScript config
├── schema.json           # JSON-LD structured data
├── zenodo.json           # Zenodo metadata
├── heartbeat.txt         # Auto-updated daily
├── mkdocs.yml            # ReadTheDocs config
├── .readthedocs.yaml     # ReadTheDocs build config
├── docs/
│   ├── index.md          # Documentation
│   └── requirements.txt
├── dataset/
│   └── network_benchmarks.csv
├── kaggle/
│   └── notebook.ipynb
├── .github/workflows/
│   ├── heartbeat.yml     # Auto-commit daily
│   └── npm-publish.yml   # Auto-publish to NPM
├── README.md
└── LICENSE
```

## Network Signal Scores

| Signal | Description | Score Range |
|--------|-------------|-------------|
| Latency | Round-trip response time quality | 0–100 |
| Bandwidth | Available throughput performance | 0–100 |
| IP Reputation | Trust and blacklist status | 0–100 |
| ASN Trust | Autonomous system reliability | 0–100 |
| Routing Quality | Path efficiency and hop analysis | 0–100 |
| Connection Stability | Jitter and packet loss consistency | 0–100 |

## Score Interpretation

| Score | Status | Action |
|-------|--------|--------|
| 0–30 | Critical | Immediate troubleshooting required |
| 31–60 | At Risk | Active monitoring needed |
| 61–80 | Healthy | Stable performance |
| 81–100 | Excellent | Optimal network condition |

## Keywords

Network Diagnostics · IP Lookup · ASN Information · ISP Geolocation · Latency Monitoring · IP Reputation · Routing Intelligence · Connection Quality · SpeedCheck

## Links

| Platform | URL |
|----------|-----|
| Website | https://speedcheck.fyi |
| Product Page | https://speedcheck.fyi/speedcheck-network-inspector |
| GitHub | https://github.com/speedcheck-fyi/speedcheck-network-inspector |
| GitHub Pages | https://speedcheck-fyi.github.io/speedcheck-network-inspector/ |
| NPM | https://npmjs.com/package/@speedcheck-fyi/network-inspector |
| Hugging Face | https://huggingface.co/datasets/speedcheck-fyi/network-inspector-benchmarks |
| Kaggle | https://kaggle.com/datasets/speedcheckfyi/network-inspector-benchmarks |
| Zenodo | https://zenodo.org/records/20797019 |
| Docs | https://speedcheck-network-inspector.readthedocs.io |

## About SpeedCheck.fyi

SpeedCheck.fyi provides real-time insights into network quality, public IP metadata, ISP details, geolocation, and connection health — designed for developers, system administrators, network engineers, and anyone troubleshooting internet performance issues.

## License

MIT — [SpeedCheck.fyi](https://speedcheck.fyi)
