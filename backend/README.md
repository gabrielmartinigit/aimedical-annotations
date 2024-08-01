# Backend

## Build & Deploy

```bash
sam validate
sam build
sam deploy --stack-name aimedical-annotations --resolve-s3 --resolve-image-repos --capabilities CAPABILITY_AUTO_EXPAND CAPABILITY_IAM
```

## Delete

```bash
sam delete --stack-name aimedical-annotations
```
