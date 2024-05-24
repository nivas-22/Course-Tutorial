
GitHub is a web-based software development project hosting platform and service. Git is a distributed version control system that is mainly used for version control. Developers may collaborate on projects, manage code repositories, and keep track of changes with GitHub.

**Features:**

- Version control:
- Repository
- Collaboration
- Branches and Merges
- Pull Requests
- Issue Tracking
- Continuous Integration and Deployment

GitHub offers a tool called GitHub Pages that makes it simple to build and publish an online website. We can use GitHub to create a repository where we can keep all the files and code for your website. After that, we may share our website with the public using GitHub Pages to create a unique URL!

GitHub Pages is a feature of GitHub that allows users to host static websites directly from their GitHub repositories. It simplifies the process of publishing web content associated with a project, user, or organization.

Here are some key points about GitHub Pages:

- **Static Websites:** HTML, CSS, and JavaScript files make up static websites, which are hosted on GitHub Pages. Databases and server-side scripting are not supported. For tasks like personal blogs, project pages, documentation, and other information that doesn’t require dynamic server processing, this makes it appropriate.
- **Free Hosting:** Public repositories can be hosted for free on GitHub Pages. GitHub Pages can also be used by private repositories, however they need to be on a premium GitHub subscription. Because it offers free hosting, it’s a desirable choice for open-source projects, individual portfolios, and documentation.
- **Automatic Builds:** Jekyll, a static site generator, is used by GitHub Pages to enable automatic builds. When enabled, Jekyll creates the necessary HTML pages by processing all of the project’s files, including Markdown files. This eliminates the need to manually write HTML for each page of a website, simplifying its creation and upkeep.
- **Custom Domains:** Instead of using the built-in GitHub Pages domain, users can set up custom domains for their sites, enabling them to use a customized web address (such as yourname.com). This helps with branding and projecting a more polished image.
- **Branch-Based Deployment:** GitHub Pages uses a specific branch (typically named gh-pages or docs) to launch the website. The branch that GitHub Pages will use to construct and launch the website is selectable by users. This makes it possible to separate the source code and website content, simplifying management.
- **Pages for Users, Organizations, and Projects:** GitHub Pages can be linked to individual repositories, user accounts, or organization accounts. You may find the user and organization pages at username.github.io and organizationname.github.io. They are linked to a particular account. Project pages can be found at organizationname.github.io/repository or username.github.io/repository, and they are linked to a specific repository.
- **HTTPS Support:** Your website can have a safe connection thanks to GitHub Pages’ support for HTTPS. Ensuring the privacy and integrity of data sent between the user and the website is of utmost importance.

**Architecture:**

![](https://miro.medium.com/v2/resize:fit:875/1*QnCcQdixwMLlVz0eE183qg.png)

**Prerequisites:**

1. A Git account.

2. An AWS Account and one Linux/Ubuntu EC2 instance with git installed.

**Steps:**

**I.** **Steps to create github repo:**

a. Log into GitHub account.

b. Click on Repositories tab -> New.

![](https://miro.medium.com/v2/resize:fit:875/1*q-_p3FgEzKJC76DqDtLc7w.png)

c. Enter Repo name as Username.github.io(eg:ABC.github.io),Description, Repository type as Public, Enable Add a README file and Click on Create Repository.

![](https://miro.medium.com/v2/resize:fit:875/1*zxlj1pc-0MibE447mEWACw.png)

d. A New repo will be created with readme file inside the repo.

![](https://miro.medium.com/v2/resize:fit:875/1*reynqNAlHEROI9pRoth27w.png)

**II.** **Steps to Push the Files into GitHub repo:**

Login to ec2 server and execute below commands

- To convert an existing, unversioned project to a Git repository or initialize a new, empty repository, execute below command to initialize

git init

- After initializing, we need clone the Git/ remote repo to copy an existing Git repository into a new local directory.

git clone https://github.com/repo_name.git

- Once cloning is completed, a new folder or directory will created automatically with Repo_name. Change to new directory.

ls  
cd repo_name

![](https://miro.medium.com/v2/resize:fit:875/1*AvJ5VAlo6hf4yJ00R5R0qg.png)

- Copy or Create Html/web page files in this directory.
- To add new files to staging area, execute below command.

git add .

- The global git username and email address are associated with the commits on all repositories on your system that don’t have repository-specific values. To set your global commit name and email address, run the `git config` command

git config - global user.name "Your Name"  
git config - global user.email "youremail@yourdomain.com"

- To check if new files are added to the staging area, execute below command:

git status

- To record the changes made to repo, we use git commit.

git commit -m "added new files"

- Once we commit, we need to push the files in git repo. We use git push command. Once you push command is executed, it asks for git Username and password (git token(classic)).

git push origin main

- After we provided git credentials, it will automatically push files into new git repo.

![](https://miro.medium.com/v2/resize:fit:875/1*3a7EU4ML0Tjj0VGOtvcgAw.png)

**III.** **Create website from Github:**

a. After files are available in the Github repository, Click on Actions. We see new Workflow deployment created.

![](https://miro.medium.com/v2/resize:fit:875/1*IEQRaLBFzJM-NEFgWcyLcA.png)

b. Click on that deployment to view the status. Once Workflow deployment is completed, Url is generated below deploy to access website.

![](https://miro.medium.com/v2/resize:fit:875/1*HvUDm-z72POHZIeeKjc71w.png)

c. Click on that URL to access webpage through internet. Our website is now accessible at `[https://username.github.io](https://username.github.io)`

![](https://miro.medium.com/v2/resize:fit:875/1*X0wlKYQHSz9pKlwrXqlnhw.png)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F3f1febe0a3c8&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40vaishnavipolichetti%2Fhost-website-on-github-pages-by-pushing-code-from-ec2-to-github-repository-3f1febe0a3c8&source=--------------------------bookmark_footer-----------)