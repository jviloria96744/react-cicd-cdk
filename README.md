## React CI/CD Template

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

Additionally, this project contains a cdk directory containing a workflow that builds out `dev` and `stg` environments on AWS. These are AWS S3 buckets which sit behind CloudFront distributions that are tied to `dev.[domain name].com` and `stg.[domain name].com` respectively. There are a few things that need to be set up manually:

- Custom Domain Name With Hosted Zone on AWS
- SSL Certificate tied to `[dev stg *].[domain name].com`. I created this before hand because this was a first attempt at a CDK project and wasn't sure about automating the certificate creation process.
- AWS User For GitHub Action Workflow. The permissions needed can be inferred through the cdk directory, but basically, creation of IAM roles, CloudFront Distributions, Route 53 Record Sets, S3 Buckets (put access as well). I may be missing some but add them as necessary.
- The following secrets in GitHub need to be created
  - AWS_ACCESS_KEY_ID / AWS_SECRET_KEY - programmatic user credentials of user created in previous step
  - AWS_REGION - default region that resources will be created in (S3 Buckets)
  - AWS_CERT_ARN - Certificate Arn of SSL Certificate, not necessary if creation of certificate is integrated in CDK deployment process
  - AWS_DOMAIN_NAME - Custom Domain Name

Below is simply the rest of the standard create-react-app README

## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.<br />
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.<br />
You will also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.<br />
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.<br />
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.<br />
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can’t go back!**

If you aren’t satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you’re on your own.

You don’t have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn’t feel obligated to use this feature. However we understand that this tool wouldn’t be useful if you couldn’t customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

### Code Splitting

This section has moved here: https://facebook.github.io/create-react-app/docs/code-splitting

### Analyzing the Bundle Size

This section has moved here: https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size

### Making a Progressive Web App

This section has moved here: https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app

### Advanced Configuration

This section has moved here: https://facebook.github.io/create-react-app/docs/advanced-configuration

### Deployment

This section has moved here: https://facebook.github.io/create-react-app/docs/deployment

### `npm run build` fails to minify

This section has moved here: https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify
