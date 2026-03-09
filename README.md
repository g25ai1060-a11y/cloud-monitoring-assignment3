# Cloud Monitoring Assignment 3

This project demonstrates CPU monitoring and stress testing using a local Alpine Linux VM and AWS CLI.

## Technologies Used
- Python
- psutil
- stress-ng
- AWS CLI
- Amazon EC2
- Alpine Linux VM

## CPU Monitoring Script

The script `monitor.py` continuously monitors CPU usage.

Example output:

Current CPU Usage: 45 %
Current CPU Usage: 82 %

## Stress Testing

CPU load was generated using:

stress-ng --cpu 4 --timeout 60s

## AWS CLI Integration

AWS CLI was configured using:

aws configure

Then EC2 instances were retrieved using:

aws ec2 describe-instances

## Author
Your Name
