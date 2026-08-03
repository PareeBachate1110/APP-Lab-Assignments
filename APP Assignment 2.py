def bold_text(func): #create decorator function
    def wrapper(report):
        return "**"+func(report)+"**"
    return wrapper

class Report:
    templates={} #create dictionary to store templates

    def __init__(self,title,content):
        self.title=title
        self.content=content

    def add_template(cls,name,template): #define func to add template to the dictionary
        cls.templates[name]=template

    def get_template(cls,name): #define func to retrieve template from dictionary
        if name in cls.templates:
            return cls.templates[name]
        else:
            return None

    def __call__(self, template_name): #magic method which makes report object in line 46 callable and this gets called when we type report("simple") or report("fancy")
        template=Report.get_template(template_name) #applies selected template
        if template:
            return template(self)
        else:
            return "Template not Found."

    def __str__(self): #creates a string representation of report object in line 46
        return f"Title: {self.title}\nContent: {self.content}"

Report.add_template = classmethod(Report.add_template) #classmethod passes the class "Report" as the first argument and applies it to all reports which will be created instead of just affecting one object 
Report.get_template = classmethod(Report.get_template)

def simple_template(report):
    return f"Report Title: {report.title}\n Report Content: {report.content}"

@bold_text
def fancy_template(report):
    return f"Report Title: {report.title}\n Report Content: {report.content}"

def main():
    Report.add_template("simple",simple_template)
    Report.add_template("fancy",fancy_template)

    report = Report("Monthly Sales","Sales Increased By 20% This Month")

    print(report("simple"))
    print(report("fancy"))

if __name__=="__main__":
    main()
