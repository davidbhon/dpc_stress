#!/bin/bash
echo AWS pricing refsa...
echo 'https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/using-ppslong.html'
echo 'https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/procedures.html'
echo 'https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2//price-changes.html'
#
jday=`date "+%Y:%j:%H:%M:%S"`
echo $jday
curl https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/index.json -o aws_v1_bulk_pricing_${jday}.json
#curl https://pricing.us-east-1.amazonaws.com/offers/v2.0/aws/index.json -o aws_v2_bulk_pricing_${jday}.json
#curl https://pricing.us-east-1.amazonaws.com/offers/v3.0/aws/index.json -o aws_v3_bulk_pricing_${jday}.json

