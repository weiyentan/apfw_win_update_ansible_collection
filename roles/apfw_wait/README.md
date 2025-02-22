# APFW Wait Role

## Fleet GitOps Considerations
While this is an Ansible role, when deploying to Kubernetes environments:
1. Use Fleet cluster selectors in your GitOps pipelines
2. Add role execution to your Fleet bundle manifests
3. Consider Tailscale ingress patterns for secure communication
