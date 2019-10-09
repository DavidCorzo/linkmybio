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

                    elif 'twitter' in inner_dict[0]:
                        twdict = inner_dict[1]
                        master.update({inner_dict[0]: inner_dict[1]})

                    elif 'instagram' in inner_dict[0]:
                        igdict = inner_dict[1]
                        master.update({inner_dict[0]: inner_dict[1]})

                    elif 'linkedin' in inner_dict[0]:
                        lidict = inner_dict[1]
                        master.update({inner_dict[0]: inner_dict[1]})
                    elif 'github' in inner_dict[0]:
                        ghdict = inner_dict[1]
                        master.update({inner_dict[0]: inner_dict[1]})

        if 'img' in key:
            img = values
            # print(values)

        if 'name' in key:
            name = values
            # print(name)

        if 'shortbio' in key:
            shortbio = values
    fb_end_date = master['facebook']['end_date'].split(',')
    fb_end_date = module.check_dates((
        int(fb_end_date[0]), int(fb_end_date[1]), int(fb_end_date[2])))
    # print(fb_end_date)

    tw_end_date = master['twitter']['end_date'].split(',')
    tw_end_date = module.check_dates(
        (int(tw_end_date[0]), int(tw_end_date[1]), int(tw_end_date[2])))
    # print(tw_end_date)

    ig_end_date = master['instagram']['end_date'].split(',')
    ig_end_date = module.check_dates(
        (int(ig_end_date[0]), int(ig_end_date[1]), int(ig_end_date[2])))
    # print(ig_end_date)

    li_end_date = master['linkedin']['end_date'].split(',')
    li_end_date = module.check_dates(
        (int(li_end_date[0]), int(li_end_date[1]), int(li_end_date[2])))
    # print(li_end_date)

    gh_end_date = master['github']['end_date'].split(',')
    gh_end_date = module.check_dates(
        (int(gh_end_date[0]), int(gh_end_date[1]), int(gh_end_date[2])))
    # print(gh_end_date)

    return render_template(
        'template.html',
        name=name,
        img=img,
        shortbio=shortbio,
        fblink=master['facebook']['link'],
        fbshow=master['facebook']['enable'],
        fbdesc=master['facebook']['description'],
        fb_end_date=fb_end_date,

        twlink=master['twitter']['link'],
        twshow=master['twitter']['enable'],
        twdesc=master['twitter']['description'],
        tw_end_date=tw_end_date,

        iglink=master['instagram']['link'],
        igshow=master['instagram']['enable'],
        igdesc=master['instagram']['description'],
        ig_end_date=ig_end_date,

        lilink=master['linkedin']['link'],
        lishow=master['linkedin']['enable'],
        lidesc=master['linkedin']['description'],
        li_end_date=li_end_date,

        ghlink=master['github']['link'],
        ghshow=master['github']['enable'],
        ghdesc=master['github']['description'],
        gh_end_date=gh_end_date
    )


if __name__ == "__main__":
    app.run(debug=True)

    # main_page()
