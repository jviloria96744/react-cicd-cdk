# React CI/CD Template

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

Additionally, this project contains a cdk directory containing a workflow that builds out `dev`, `stg` and `prod` environments on AWS. These are AWS S3 buckets which sit behind CloudFront distributions that are tied to `env*.my-example-domain.com` respectively. There are a few things that need to be set up manually:

- Custom Domain Name With Hosted Zone on AWS
- SSL Certificate tied to `env*.my-example-domain.com`. I created this before hand because this was a first attempt at a CDK project and I wasn't sure about automating the certificate creation process, i.e. potential to repeatedly create new certificates during testing. It could be created as a separate stack with a region of `us-east-1` and stored in the parameter store and referenced in the standard stack creation process.
- AWS User For GitHub Action Workflow. The permissions needed can be inferred through the cdk directory, but basically, creation of IAM roles, CloudFront Distributions, Route 53 Record Sets, S3 Buckets (put access as well). I may be missing some but add them as necessary.
- The following secrets in GitHub need to be created
  - AWS_ACCESS_KEY_ID / AWS_SECRET_KEY - programmatic user credentials of user created in previous step
  - AWS_REGION - default region that resources will be created in (S3 Buckets)
  - AWS_CERT_ARN - Certificate Arn of SSL Certificate, not necessary if creation of certificate is integrated in CDK deployment process
  - AWS_DOMAIN_NAME - Custom Domain Name

## Development Workflow

- Any push to branches of the form "feature\*" trigger the `test-only` job which runs any front-end tests that exist. Currently nothing is done in the event of test failure.
- Any push or pull request into master triggers the `build` job which deploys the static site onto AWS (`dev`), procuring the resources if necessary, using CDK, after running any front-end tests.
- Any `tag` push triggers the `build` job as above for the `stg` environment with additional steps to store an artifact of the build into an artifacts bucket for use in `prod` deployments
- A manual job exists that can be triggered through GitHub that takes a tag as input and deploys the appropriate artifact into the `prod` bucket from the artifact bucket mentioned in the previous step

## Notes/Possible Enhancement Areas

- The manual job was to simulate an environment where some manual sign-off from business was required for deployments to production
- Efficiency gains could be had by re-writing the cdk portion of the template in JavaScript (avoidance of multiple run times in GitHub Action workflow). I simply chose Python because of personal preference
- Since the CloudFormation Stack Names are more or less fixed (up to an environment parameter), it may be possible to conditionally run the CDK portion (potentially avoiding installing all the needed dependencies). Currently, we must execute those steps to get the dynamically generated bucket/distribution names. This can possibly be replaced by a CloudFormation describe command and parsing of the JSON after
- I believe this can be extended to work on multiple accounts, e.g. separate `dev`, `stg` and `prod` accounts by using separate sets of AWS secrets. Alternatively, it would be interesting to try and set one secret with all the account config as a JSON string and parse it using an environment variable derived from the event type, though I am not sure what restrictions exist on GitHub Secrets.
- I am still not sure what CDK or GitHub Action best practices are. I experimented with test variables in the GitHub Action template to shut things down when testing the pipeline. I can also imagine using the environment variable to shut down/activate some of the logging steps that included in the pipeline. As far as CDK, I considered splitting the `StaticSiteStack` class into a few different pieces, with individual resources having their own module. I can imagine with a larger stack, that being a necessity.

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
