#!/bin/bash

echo "::set-env name=STACK::$(jq '.app' cdk.json)"
echo "::set-env name=STACK2::Test"