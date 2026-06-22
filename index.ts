#!/usr/bin/env node

interface NetworkInput {
  targetIp: string;
  latency: number;
  bandwidth: number;
  ipReputation: number;
  asnTrust: number;
  routingQuality: number;
  connectionStability: number;
}

interface NetworkOutput {
  targetIp: string;
  latencyScore: number;
  bandwidthScore: number;
  ipReputationScore: number;
  asnTrustScore: number;
  routingQualityScore: number;
  connectionStabilityScore: number;
  overallNetworkHealth: number;
  prioritySignal: string;
}

function getStatus(score: number): string {
  if (score <= 30) return "Critical";
  if (score <= 60) return "At Risk";
  if (score <= 80) return "Healthy";
  return "Excellent";
}

function getPrioritySignal(scores: Record<string, number>): string {
  const labels: Record<string, string> = {
    latency: "Latency",
    bandwidth: "Bandwidth",
    ipReputation: "IP Reputation",
    asnTrust: "ASN Trust",
    routingQuality: "Routing Quality",
    connectionStability: "Connection Stability",
  };
  const lowest = Object.entries(scores).reduce((a, b) => a[1] < b[1] ? a : b);
  return `${labels[lowest[0]]} (${lowest[1]}/100 — act first)`;
}

export function inspectNetwork(input: NetworkInput): NetworkOutput {
  const scores = {
    latency: input.latency,
    bandwidth: input.bandwidth,
    ipReputation: input.ipReputation,
    asnTrust: input.asnTrust,
    routingQuality: input.routingQuality,
    connectionStability: input.connectionStability,
  };
  const overallNetworkHealth = Math.round(
    Object.values(scores).reduce((a, b) => a + b, 0) / 6
  );
  return {
    targetIp: input.targetIp,
    latencyScore: input.latency,
    bandwidthScore: input.bandwidth,
    ipReputationScore: input.ipReputation,
    asnTrustScore: input.asnTrust,
    routingQualityScore: input.routingQuality,
    connectionStabilityScore: input.connectionStability,
    overallNetworkHealth,
    prioritySignal: getPrioritySignal(scores),
  };
}

const args = process.argv.slice(2);
const targetIp = args[0] || "192.0.2.1";
const latency = parseInt(args[1]) || 85;
const bandwidth = parseInt(args[2]) || 70;
const ipReputation = parseInt(args[3]) || 90;
const asnTrust = parseInt(args[4]) || 65;
const routingQuality = parseInt(args[5]) || 80;
const connectionStability = parseInt(args[6]) || 75;

const result = inspectNetwork({
  targetIp, latency, bandwidth, ipReputation,
  asnTrust, routingQuality, connectionStability,
});

console.log(`Target IP: ${result.targetIp}`);
console.log("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━");
console.log(`Latency Score:               ${result.latencyScore}/100  [${getStatus(result.latencyScore)}]`);
console.log(`Bandwidth Score:             ${result.bandwidthScore}/100  [${getStatus(result.bandwidthScore)}]`);
console.log(`IP Reputation Score:         ${result.ipReputationScore}/100  [${getStatus(result.ipReputationScore)}]`);
console.log(`ASN Trust Score:             ${result.asnTrustScore}/100  [${getStatus(result.asnTrustScore)}]`);
console.log(`Routing Quality Score:       ${result.routingQualityScore}/100  [${getStatus(result.routingQualityScore)}]`);
console.log(`Connection Stability Score:  ${result.connectionStabilityScore}/100  [${getStatus(result.connectionStabilityScore)}]`);
console.log("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━");
console.log(`Overall Network Health:      ${result.overallNetworkHealth}/100`);
console.log(`Priority Signal:             ${result.prioritySignal}`);
