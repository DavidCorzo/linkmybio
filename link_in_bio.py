from flask import Flask, render_template
import module

app = Flask(__name__)


@app.route("/")
def main_page():
    master_unfiltered = module.open_master()
    master = {}
    img = None
    shortbio = None
    for key, values in master_unfiltered.items():
        if 'links' in key:
            for link_dicts in values:
                for inner_dict in link_dicts.items():
                    if 'facebook' in inner_dict[0]:
                        fbdict = inner_dict[1]
                        master.update({inner_dict[0]: inner_dict[1]})
                        # print(fbdict)
                    elif 'twitter' in inner_dict[0]:
                        twdict = inner_dict[1]
                        master.update({inner_dict[0]: inner_dict[1]})
                        # print(twdict)
                    elif 'instagram' in inner_dict[0]:
                        igdict = inner_dict[1]
                        master.update({inner_dict[0]: inner_dict[1]})
                        # print(igdict)
                    elif 'linkedin' in inner_dict[0]:
                        lidict = inner_dict[1]
                        master.update({inner_dict[0]: inner_dict[1]})
                        # print(lidict)
        if 'img' in key:
            img = values
            # print(values)

        if 'name' in key:
            name = values
            # print(name)

        if 'shortbio' in key:
            shortbio = values

    return render_template(
        'template.html',
        name=name,
        img=img,
        shortbio=shortbio,
        fblink=master['facebook']['link'],
        fbshow=master['facebook']['enable'],
        fbdesc=master['facebook']['description'],
        twlink=master['twitter']['link'],
        twshow=master['twitter']['enable'],
        twdesc=master['twitter']['description'],
        iglink=master['instagram']['link'],
        igshow=master['instagram']['enable'],
        igdesc=master['instagram']['description'],
        lilink=master['linkedin']['link'],
        lishow=master['linkedin']['enable'],
        lidesc=master['linkedin']['description'])


if __name__ == "__main__":
    app.run(debug=True)

    # main_page()
