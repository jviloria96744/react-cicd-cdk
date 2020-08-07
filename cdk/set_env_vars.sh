#!/bin/bash

export FILE=cdk-deploy-output.json
echo "::set-env name=STACK::$(jq keys_unsorted[] $FILE)"
export STACK=$(jq keys_unsorted[] $FILE) 

function remove_quotes {
    echo $1 | tr -d '"'
}

echo "::set-env name=DIST_ID::$(remove_quotes $(jq .$STACK.distid $FILE))"
echo "::set-env name=BUCKET::$(remove_quotes $(jq .$STACK.sitebucketname $FILE))"
echo "::set-env name=ARTIFACT_BUCKET::$(remove_quotes $(jq .$STACK.artifactbucketname $FILE))"