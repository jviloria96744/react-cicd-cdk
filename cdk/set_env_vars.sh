#!/bin/bash

echo "::set-env name=STACK::$(jq keys_unsorted[] cdk-deploy-output.json)"
export STACK=$(jq keys_unsorted[] cdk-deploy-output.json) 

function remove_quotes {
    echo $1 | tr -d '"'
}

echo "::set-env name=DIST_ID::$(remove_quotes jq .$STACK.distid cdk-deploy-output.json)"
echo "::set-env name=BUCKET::$(remove_quotes jq .$STACK.sitebucketname cdk-deploy-output.json)"
echo "::set-env name=ARTIFACT_BUCKET::$(remove_quotes jq .$STACK.artifactbucketname cdk-deploy-output.json)"