#!/bin/bash

# Start nginx in the background
nginx

# Start nginx-prometheus-exporter in the foreground
nginx-prometheus-exporter -nginx.scrape-uri http://127.0.0.1/stub_status