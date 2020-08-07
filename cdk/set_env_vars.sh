#!/bin/bash

echo "::set-env name=STACK::$(jq keys_unsorted[] cdk-deploy-output.json)"
export STACK=$(jq keys_unsorted[] cdk-deploy-output.json) 
echo "::set-env name=DIST_ID::$(jq .$STACK.distid cdk-deploy-output.json)"
echo "::set-env name=BUCKET::$(jq .$STACK.sitebucketname cdk-deploy-output.json)"
echo "::set-env name=ARTIFACT_BUCKET::$(jq .$STACK.artifactbucketname cdk-deploy-output.json)"