#!/usr/bin/env python3
"""
SpeedCheck Network Inspector
A lightweight network diagnostics bot that helps analyze internet connectivity,
latency, bandwidth performance, IP reputation, ASN information, and routing
intelligence.
https://speedcheck.fyi | https://speedcheck.fyi/speedcheck-network-inspector
"""

import sys


def get_status(score: int) -> str:
    if score <= 30:
        return "Critical"
    elif score <= 60:
        return "At Risk"
    elif score <= 80:
        return "Healthy"
    return "Excellent"


def get_priority_signal(scores: dict) -> str:
    labels = {
        "latency": "Latency",
        "bandwidth": "Bandwidth",
        "ip_reputation": "IP Reputation",
        "asn_trust": "ASN Trust",
        "routing_quality": "Routing Quality",
        "connection_stability": "Connection Stability",
    }
    lowest_key = min(scores, key=scores.get)
    return f"{labels[lowest_key]} ({scores[lowest_key]}/100 — act first)"


def inspect_network(
    target_ip: str,
    latency: int = 85,
    bandwidth: int = 70,
    ip_reputation: int = 90,
    asn_trust: int = 65,
    routing_quality: int = 80,
    connection_stability: int = 75,
) -> dict:
    """
    Inspect and score network diagnostic signals separately.

    Args:
        target_ip: Target IP address or hostname
        latency: Latency score (0-100)
        bandwidth: Bandwidth score (0-100)
        ip_reputation: IP reputation score (0-100)
        asn_trust: ASN trust score (0-100)
        routing_quality: Routing quality score (0-100)
        connection_stability: Connection stability score (0-100)

    Returns:
        dict with individual signal scores and overall network health
    """
    scores = {
        "latency": latency,
        "bandwidth": bandwidth,
        "ip_reputation": ip_reputation,
        "asn_trust": asn_trust,
        "routing_quality": routing_quality,
        "connection_stability": connection_stability,
    }
    overall_network_health = round(sum(scores.values()) / 6)

    return {
        "target_ip": target_ip,
        "latency_score": latency,
        "bandwidth_score": bandwidth,
        "ip_reputation_score": ip_reputation,
        "asn_trust_score": asn_trust,
        "routing_quality_score": routing_quality,
        "connection_stability_score": connection_stability,
        "overall_network_health": overall_network_health,
        "priority_signal": get_priority_signal(scores),
    }


if __name__ == "__main__":
    target_ip = sys.argv[1] if len(sys.argv) > 1 else "192.0.2.1"
    latency = int(sys.argv[2]) if len(sys.argv) > 2 else 85
    bandwidth = int(sys.argv[3]) if len(sys.argv) > 3 else 70
    ip_reputation = int(sys.argv[4]) if len(sys.argv) > 4 else 90
    asn_trust = int(sys.argv[5]) if len(sys.argv) > 5 else 65
    routing_quality = int(sys.argv[6]) if len(sys.argv) > 6 else 80
    connection_stability = int(sys.argv[7]) if len(sys.argv) > 7 else 75

    result = inspect_network(
        target_ip, latency, bandwidth, ip_reputation,
        asn_trust, routing_quality, connection_stability
    )

    print(f"Target IP: {result['target_ip']}")
    print("=" * 45)
    print(f"Latency Score:               {result['latency_score']}/100  [{get_status(result['latency_score'])}]")
    print(f"Bandwidth Score:             {result['bandwidth_score']}/100  [{get_status(result['bandwidth_score'])}]")
    print(f"IP Reputation Score:         {result['ip_reputation_score']}/100  [{get_status(result['ip_reputation_score'])}]")
    print(f"ASN Trust Score:             {result['asn_trust_score']}/100  [{get_status(result['asn_trust_score'])}]")
    print(f"Routing Quality Score:       {result['routing_quality_score']}/100  [{get_status(result['routing_quality_score'])}]")
    print(f"Connection Stability Score:  {result['connection_stability_score']}/100  [{get_status(result['connection_stability_score'])}]")
    print("=" * 45)
    print(f"Overall Network Health:      {result['overall_network_health']}/100")
    print(f"Priority Signal:             {result['priority_signal']}")
