#!/bin/bash

export FILE=cdk-deploy-output.json
export STACK=$(jq keys_unsorted[] $FILE)
echo "::set-env name=STACK::$STACK" 

function remove_quotes {
    echo $1 | tr -d '"'
}

echo "::set-env name=DIST_ID::$(remove_quotes $(jq .$STACK.distid $FILE))"
echo "::set-env name=BUCKET::$(remove_quotes $(jq .$STACK.sitebucketname $FILE))"