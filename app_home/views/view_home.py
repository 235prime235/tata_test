import os

def view_home():

    template_header_file = os.getcwd() + "/templates/header.html"
    template_navbar_file = os.getcwd() + "/templates/main_navbar.html"
    template_footer_file = os.getcwd() + "/templates/footer.html"

    with open (template_header_file, "r") as navfile:
        str_header = navfile.read()
    
    with open (template_navbar_file, "r") as navfile:
        str_navbar = navfile.read()

    with open (template_footer_file, "r") as navfile:
        str_footer = navfile.read()

##HEADER
    str_page = str_header
    str_page = str_page + str_navbar

##BODY
    str_page = str_page + """
    <div class="site-container">
    <h2>Home page</h2>
    </div>
    """

##FOOTER
    str_page = str_page + str_footer

    return str_page 