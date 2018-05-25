import os
import jinja2

def render(tpl_path, context):
    path, filename = os.path.split(tpl_path)
    return jinja2.Environment(
        loader=jinja2.FileSystemLoader(path or './')
    ).get_template(filename).render(context)

context = {
  'callysto_html_url': "http://hub.callysto.ca",
  'callysto_html_domain': "callysto.ca",
  'callysto_html_hostname': "hub.callysto.ca",
  'callysto_html_support_email': "support@callysto.ca",
  'callysto_html_logout_message': "You have been logged out of your Jupyter Session",
  'callysto_html_terms': """By using this service you are indicating that you agree with the Rapid Access
   Cloud <a href="http://www.cybera.ca/policies/acceptable-use-policy-cloud-services/">acceptable
   use policy</a> and <a href="http://www.cybera.ca/wp-content/uploads/2018/05/Rapid-Access-Cloud-Terms-of-Service.pdf">terms
   of service</a>."""
}

pages = ['_site/index.html', '_site/logout/index.html']

for page in pages:
    with open(page,'r+') as f:
        template = f.read()
        
        result = render(page, context=context)
        f.seek(0)
        f.write(result)

