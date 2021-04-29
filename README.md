# python-unittest-htmlTestRunner-GitHub-Action-demo

This demo shows how to use **Github Action** to automatically generate elegant HTML reports for python unittest whenever there is pull request or push.


If you want to replace GitHub Action with Jenkins, you can view the video explaination here [https://www.youtube.com/watch?v=IgaBnNzCGfo](https://www.youtube.com/watch?v=IgaBnNzCGfo), the repository here [jenkins-demo](https://github.com/Spycsh/python-unittest-htmlTestRunner-jenkins-demo)

## Workflow

In the `.github/workflows` folder, you can see the `main.yml` which contains the whole work flow you need to automatically generate elegant HTML reports for python unittest whenever there is pull request or push. If you are not familiar with GitHub Action,  you can view [https://docs.github.com/en/actions/reference/workflow-syntax-for-github-actions](https://docs.github.com/en/actions/reference/workflow-syntax-for-github-actions). You can write your source code in `/src` and test code in `test`.

If you have viewed the video of the same topic about Jenkins, I would say this repo use GitHub Action to ease testers from the complex settings of their Jenkins. Users can see the results in `result.html` after each push or PR to their repo. 

So Jenkins and GitHub Action, which would you prefer :smirk: ?
