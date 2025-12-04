from playwright.sync_api import sync_playwright
import pandas as pd

EMAIL = ""
PASSWORD = ""

COMPANY_URLS = [
    "https://vrexpogreece.com/en/exhibitor/3830/plasis-real-estate-kai-development",
    "https://vrexpogreece.com/en/exhibitor/7368/eurobank",
    "https://vrexpogreece.com/en/exhibitor/7785/lezanco-properties-limited",
    "https://vrexpogreece.com/en/exhibitor/7403/luxkaieasy",
    "https://vrexpogreece.com/en/exhibitor/7414/mibs-group",
    "https://vrexpogreece.com/en/exhibitor/7760/spitogatos",
    "https://vrexpogreece.com/en/exhibitor/7802/ethniki-trapeza",
    "https://vrexpogreece.com/en/exhibitor/7766/piraios",
    "https://vrexpogreece.com/en/exhibitor/4826/3d-360-vr-daedalus",
    "https://vrexpogreece.com/en/exhibitor/7409/3d-path",
    "https://vrexpogreece.com/en/exhibitor/7446/a-syggrou",
    "https://vrexpogreece.com/en/exhibitor/7607/ambience-services",
    "https://vrexpogreece.com/en/exhibitor/7535/arcus-real-estate",
    "https://vrexpogreece.com/en/exhibitor/7759/ask-wire",
    "https://vrexpogreece.com/en/exhibitor/7396/aspect-photo",
    "https://vrexpogreece.com/en/exhibitor/7396/aspect-photo",
    "https://vrexpogreece.com/en/exhibitor/3851/aspis-real-estate",
    "https://vrexpogreece.com/en/exhibitor/7541/sillogos-mesiton-thessalonikis-smasth",
    "https://vrexpogreece.com/en/exhibitor/7812/astrit-development",
    "https://vrexpogreece.com/en/exhibitor/7621/athenean-agency",
    "https://vrexpogreece.com/en/exhibitor/3852/atlas-group",
    "https://vrexpogreece.com/en/exhibitor/7803/attica-bank",
    "https://vrexpogreece.com/en/exhibitor/3837/attica-house",
    "https://vrexpogreece.com/en/exhibitor/7811/atticabank-properties",
    "https://vrexpogreece.com/en/exhibitor/7401/bbf%3A-greece",
    "https://vrexpogreece.com/en/exhibitor/7729/blackhawk-anonimi-etairia-simvouli-michaniki",
    "https://vrexpogreece.com/en/exhibitor/7347/blueground",
    "https://vrexpogreece.com/en/exhibitor/7363/blupeak-estate-analytics",
    "https://vrexpogreece.com/en/exhibitor/7736/breek.gr",
    "https://vrexpogreece.com/en/exhibitor/3863/brokerhouse",
    "https://vrexpogreece.com/en/exhibitor/7580/casa-futura-real-estate",
    "https://vrexpogreece.com/en/exhibitor/7619/central-greece-gems",
    "https://vrexpogreece.com/en/exhibitor/7378/centro-kitchen",
    "https://vrexpogreece.com/en/exhibitor/4150/check-in",
    "https://vrexpogreece.com/en/exhibitor/7531/cherry-investments-sa",
    "https://vrexpogreece.com/en/exhibitor/4611/city-1-real-estate",
    "https://vrexpogreece.com/en/exhibitor/7649/cm-real-estate-myrsini-chalafti",
    "https://vrexpogreece.com/en/exhibitor/4615/corpus-real-estate-legal-firm",
    "https://vrexpogreece.com/en/exhibitor/7727/cp-mortgage-advisors",
    "https://vrexpogreece.com/en/exhibitor/7614/cretaestate",
    "https://vrexpogreece.com/en/exhibitor/7737/crisos-group",
    "https://vrexpogreece.com/en/exhibitor/7731/cst-architects",
    "https://vrexpogreece.com/en/exhibitor/7366/d.-n.-anagnostopoulos-kai-sinergates",
    "https://vrexpogreece.com/en/exhibitor/7780/day-one-growth-igniters",
    "https://vrexpogreece.com/en/exhibitor/7571/delatolas-express-cargo",
    "https://vrexpogreece.com/en/exhibitor/7581/delfi-properties-hellas",
    "https://vrexpogreece.com/en/exhibitor/7528/dervenis-real-estate",
    "https://vrexpogreece.com/en/exhibitor/7796/destsetters",
    "https://vrexpogreece.com/en/exhibitor/7639/dg-mesitiki-lemnos",
    "https://vrexpogreece.com/en/exhibitor/7615/diamesolavisi-real-estate-kai-brokers",
    "https://vrexpogreece.com/en/exhibitor/7603/digimark-a.e.",
    "https://vrexpogreece.com/en/exhibitor/7381/ipiresies-diadiktiou-aboutnet",
    "https://vrexpogreece.com/en/exhibitor/7356/divine-property-s.a.",
    "https://vrexpogreece.com/en/exhibitor/7601/dkg-development",
    "https://vrexpogreece.com/en/exhibitor/7393/dontas-real-estate",
    "https://vrexpogreece.com/en/exhibitor/7355/east-to-west-real-estate",
    "https://vrexpogreece.com/en/exhibitor/7570/ecredit",
    "https://vrexpogreece.com/en/exhibitor/7613/elaia-real-estate",
    "https://vrexpogreece.com/en/exhibitor/7734/elata-xirolivadou",
    "https://vrexpogreece.com/en/exhibitor/7726/elite-investments",
    "https://vrexpogreece.com/en/exhibitor/4393/ellika-real-estate",
    "https://vrexpogreece.com/en/exhibitor/7889/energy-land-parnassos-real-estate",
    "https://vrexpogreece.com/en/exhibitor/3839/epsilon-team",
    "https://vrexpogreece.com/en/exhibitor/7609/equity-stones",
    "https://vrexpogreece.com/en/exhibitor/3824/estia-developments",
    "https://vrexpogreece.com/en/exhibitor/7379/euperty-olokliromenes-ipiresies-akiniton",
    "https://vrexpogreece.com/en/exhibitor/7606/fiabci-greece",
    "https://vrexpogreece.com/en/exhibitor/4394/focus-properties",
    "https://vrexpogreece.com/en/exhibitor/7399/forte-systems",
    "https://vrexpogreece.com/en/exhibitor/7364/fortunet-hellas",
    "https://vrexpogreece.com/en/exhibitor/7767/free-architects",
    "https://vrexpogreece.com/en/exhibitor/7763/dikigoriko-grafio-georgaraki-d.-papadopoulos-ch.",
    "https://vrexpogreece.com/en/exhibitor/7392/dikigoriko-grafio-giorgos-petrou",
    "https://vrexpogreece.com/en/exhibitor/7610/giakoumidis-properties",
    "https://vrexpogreece.com/en/exhibitor/7784/giant-stride",
    "https://vrexpogreece.com/en/exhibitor/7577/gim-agency",
    "https://vrexpogreece.com/en/exhibitor/7514/global-concept",
    "https://vrexpogreece.com/en/exhibitor/7372/go-greece-real-estate-development",
    "https://vrexpogreece.com/en/exhibitor/4395/golden-home",
    "https://vrexpogreece.com/en/exhibitor/7569/golden-star",
    "https://vrexpogreece.com/en/exhibitor/7573/greca-developments",
    "https://vrexpogreece.com/en/exhibitor/3832/greek-home-real-estate",
    "https://vrexpogreece.com/en/exhibitor/7400/grekodom-development",
    "https://vrexpogreece.com/en/exhibitor/7602/halkidiki-realtors",
    "https://vrexpogreece.com/en/exhibitor/7583/heracles-real-estate-kai-development",
    "https://vrexpogreece.com/en/exhibitor/7389/hill-dickinson-international",
    "https://vrexpogreece.com/en/exhibitor/4823/hosthub",
    "https://vrexpogreece.com/en/exhibitor/7358/housem.a.n.-brokers",
    "https://vrexpogreece.com/en/exhibitor/7383/i-auction",
    "https://vrexpogreece.com/en/exhibitor/7645/i-lisis",
    "https://vrexpogreece.com/en/exhibitor/3825/iarts",
    "https://vrexpogreece.com/en/exhibitor/7604/icomm",
    "https://vrexpogreece.com/en/exhibitor/7638/ikaria-real-estate",
    "https://vrexpogreece.com/en/exhibitor/3853/ims-fc",
    "https://vrexpogreece.com/en/exhibitor/3826/inovart-properties",
    "https://vrexpogreece.com/en/exhibitor/7382/invest-greece-solomon",
    "https://vrexpogreece.com/en/exhibitor/3840/irg-pro-investment-and-residency",
    "https://vrexpogreece.com/en/exhibitor/7611/israel-greece-chamber-of-commerce-and-industry",
    "https://vrexpogreece.com/en/exhibitor/3827/jk-poulsen-property-investment-group",
    "https://vrexpogreece.com/en/exhibitor/7576/kappasigma-partners",
    "https://vrexpogreece.com/en/exhibitor/7751/kep-energias",
    "https://vrexpogreece.com/en/exhibitor/7644/ktimatomesitiko-grafio-kokarakis-ioannis",
    "https://vrexpogreece.com/en/exhibitor/7762/koligas",
    "https://vrexpogreece.com/en/exhibitor/7534/ktitors",
    "https://vrexpogreece.com/en/exhibitor/7749/kube-contractors",
    "https://vrexpogreece.com/en/exhibitor/7756/landmark",
    "https://vrexpogreece.com/en/exhibitor/7640/lemnos-real-estate",
    "https://vrexpogreece.com/en/exhibitor/7398/leomar-real-estate-corfu-lpc",
    "https://vrexpogreece.com/en/exhibitor/7626/sillogos-mesiton-astikon-simvaseon-lesvou",
    "https://vrexpogreece.com/en/exhibitor/7579/limar-homes",
    "https://vrexpogreece.com/en/exhibitor/7518/link-simvoulevtiki-mon.ae",
    "https://vrexpogreece.com/en/exhibitor/4614/lion-real-estate",
    "https://vrexpogreece.com/en/exhibitor/3828/magna-real-estate",
    "https://vrexpogreece.com/en/exhibitor/7529/mandalianou-estate-and-partners",
    "https://vrexpogreece.com/en/exhibitor/7643/mesitiko-grafio-markos-kounellis",
    "https://vrexpogreece.com/en/exhibitor/7728/metroland-real-estate",
    "https://vrexpogreece.com/en/exhibitor/7567/mirum-group",
    "https://vrexpogreece.com/en/exhibitor/7360/moonshot-productions",
    "https://vrexpogreece.com/en/exhibitor/7568/morcos-real-estate",
    "https://vrexpogreece.com/en/exhibitor/7572/nantia-mpimpa-holistic-real-estate-agent",
    "https://vrexpogreece.com/en/exhibitor/7395/nasco",
    "https://vrexpogreece.com/en/exhibitor/7397/naxian-land",
    "https://vrexpogreece.com/en/exhibitor/3841/nova-real-estate",
    "https://vrexpogreece.com/en/exhibitor/7754/ikodomin",
    "https://vrexpogreece.com/en/exhibitor/7578/omran-real-estate",
    "https://vrexpogreece.com/en/exhibitor/3829/orizor",
    "https://vrexpogreece.com/en/exhibitor/7774/orizory",
    "https://vrexpogreece.com/en/exhibitor/7792/pafilia-property-developers",
    "https://vrexpogreece.com/en/exhibitor/4396/panflow",
    "https://vrexpogreece.com/en/exhibitor/7641/paros-prime-properties",
    "https://vrexpogreece.com/en/exhibitor/7772/partnernet",
    "https://vrexpogreece.com/en/exhibitor/7888/pavlakis-real-estate",
    "https://vrexpogreece.com/en/exhibitor/7743/pavlidis-realty",
    "https://vrexpogreece.com/en/exhibitor/7739/peterson%E2%80%99s-group",
    "https://vrexpogreece.com/en/exhibitor/7769/placy",
    "https://vrexpogreece.com/en/exhibitor/7402/plus-properties-greece",
    "https://vrexpogreece.com/en/exhibitor/7608/klidi",
    "https://vrexpogreece.com/en/exhibitor/4575/potamianos-mesitiko-grafio",
    "https://vrexpogreece.com/en/exhibitor/7413/pro-virtual-tour",
    "https://vrexpogreece.com/en/exhibitor/7624/propertycheck.grmoschopoulou-kai-associates-law-office",
    "https://vrexpogreece.com/en/exhibitor/7352/prosperty",
    "https://vrexpogreece.com/en/exhibitor/7371/qobrix",
    "https://vrexpogreece.com/en/exhibitor/7533/re-max-kanavos",
    "https://vrexpogreece.com/en/exhibitor/3831/re-max-creative",
    "https://vrexpogreece.com/en/exhibitor/7370/re-max-hellas",
    "https://vrexpogreece.com/en/exhibitor/7380/re-max-ideal-naxos",
    "https://vrexpogreece.com/en/exhibitor/7530/re-max-metron",
    "https://vrexpogreece.com/en/exhibitor/7362/re-max-properties-investment",
    "https://vrexpogreece.com/en/exhibitor/7515/re-max-today",
    "https://vrexpogreece.com/en/exhibitor/7517/re-max-welcome",
    "https://vrexpogreece.com/en/exhibitor/7532/real-earth",
    "https://vrexpogreece.com/en/exhibitor/7771/real-estate-consultans-kai-investments",
    "https://vrexpogreece.com/en/exhibitor/7750/real-estate-for-you",
    "https://vrexpogreece.com/en/exhibitor/7536/real-praxis",
    "https://vrexpogreece.com/en/exhibitor/7740/realflow-agency",
    "https://vrexpogreece.com/en/exhibitor/7330/realty-iq",
    "https://vrexpogreece.com/en/exhibitor/7761/realty-world",
    "https://vrexpogreece.com/en/exhibitor/7776/red-olive-developments",
    "https://vrexpogreece.com/en/exhibitor/7625/periferia-voriou-aigaiou",
    "https://vrexpogreece.com/en/exhibitor/7539/remax-morphi",
    "https://vrexpogreece.com/en/exhibitor/7775/rentylife-investements",
    "https://vrexpogreece.com/en/exhibitor/7377/revithis-real-estate",
    "https://vrexpogreece.com/en/exhibitor/7375/riviera-hellas",
    "https://vrexpogreece.com/en/exhibitor/7459/sabbianco-properties",
    "https://vrexpogreece.com/en/exhibitor/7650/sappho-estate",
    "https://vrexpogreece.com/en/exhibitor/7416/sarantis-nikolaos-ikodomiki-kai-sia-ee",
    "https://vrexpogreece.com/en/exhibitor/7367/sbhomes",
    "https://vrexpogreece.com/en/exhibitor/7770/siotos-real-estate",
    "https://vrexpogreece.com/en/exhibitor/7723/smart-house",
    "https://vrexpogreece.com/en/exhibitor/7735/smarthouse-insurance-real-estate",
    "https://vrexpogreece.com/en/exhibitor/7837/starworld-enterprises",
    "https://vrexpogreece.com/en/exhibitor/7755/sun-yield-hellas",
    "https://vrexpogreece.com/en/exhibitor/7670/themeliotechniki-real-estate-group",
    "https://vrexpogreece.com/en/exhibitor/7359/thermaides",
    "https://vrexpogreece.com/en/exhibitor/7742/titlos.com",
    "https://vrexpogreece.com/en/exhibitor/7733/toptopo-real-estate",
    "https://vrexpogreece.com/en/exhibitor/7778/tzeli-real-estate",
    "https://vrexpogreece.com/en/exhibitor/7548/unhcr-greece",
    "https://vrexpogreece.com/en/exhibitor/7540/uniliv",
    "https://vrexpogreece.com/en/exhibitor/3862/union-properties",
    "https://vrexpogreece.com/en/exhibitor/7394/upyachting",
    "https://vrexpogreece.com/en/exhibitor/7387/valenci-luxury-developers",
    "https://vrexpogreece.com/en/exhibitor/3833/vkbnb",
    "https://vrexpogreece.com/en/exhibitor/7537/vsofa",
    "https://vrexpogreece.com/en/exhibitor/4240/vst-group",
    "https://vrexpogreece.com/en/exhibitor/7616/well-living-real-estate",
    "https://vrexpogreece.com/en/exhibitor/7408/william-haddad-properties-whp",
    "https://vrexpogreece.com/en/exhibitor/7738/wonder-international-realty",
    "https://vrexpogreece.com/en/exhibitor/7799/wonderlab-productions",
    "https://vrexpogreece.com/en/exhibitor/7617/yp-design",
    "https://vrexpogreece.com/en/exhibitor/7801/ipiresia-axiopiisis-akinitis-perousias-enoplon-dinameon",
    "https://vrexpogreece.com/en/exhibitor/7620/zafido-hellas",
    "https://vrexpogreece.com/en/exhibitor/7618/zarodimos-properties",
    "https://vrexpogreece.com/en/exhibitor/7575/zirogiannis-real-estate",
    "https://vrexpogreece.com/en/exhibitor/7777/zkk-kai-associates"
]


# ---------------- LOGIN ---------------- #

def login(page):
    print("🔐 Opening login page...")
    page.goto("https://vrexpogreece.com/en/account", wait_until="domcontentloaded")
    page.wait_for_timeout(2000)

    print("📌 Filling login form...")
    try:
        page.fill("#authform-username", EMAIL)
        page.fill("input[name='AuthForm[password]']", PASSWORD)
        print("➡ Clicking submit...")
        page.click("button[type='submit']")
    except Exception as e:
        print("❌ Could not fill form:", e)

    print("⏳ Waiting for post-login state...")
    page.wait_for_timeout(4000)

    content = page.content().lower()
    current_url = page.url.lower()
    print("📜 DEBUG — URL after login:", current_url)

    # Heuristics: if any of these appear, we assume login ok
    if (
        "logout" in content or
        "live chat" in content or
        "profile" in content or
        "dashboard" in content or
        "exhibitors" in current_url or
        "welcome" in content
    ):
        print("🎉 LOGIN SUCCESS")
        return True

    print("⚠ Login not clearly confirmed, but continuing (browser shows you are logged in).")
    return True


# ---------------- HELPERS ---------------- #

def _clean_email_from_href(href: str) -> str:
    if not href:
        return ""
    href = href.strip()
    if href.lower().startswith("mailto:"):
        href = href.split(":", 1)[1]
    return href.split("?", 1)[0].strip()


def _clean_phone_from_href(href: str) -> str:
    if not href:
        return ""
    href = href.strip()
    if href.lower().startswith("tel:"):
        href = href.split(":", 1)[1]
    return href.strip()


# ---------------- COMPANY CONTACT ---------------- #

def extract_company_contact(page):
    """
    Extract company name, phone, email, website, from the Contact card,
    NOT from the global top header.
    """
    # Name: main title on page
    if page.locator("h1.font-size-xl").count():
        name = page.locator("h1.font-size-xl").first.inner_text().strip()
    elif page.locator("h1").count():
        name = page.locator("h1").first.inner_text().strip()
    else:
        name = ""

    # Find the card that has the 'Contact' header
    contact_card = page.locator(
        "//h4[contains(normalize-space(.),'Contact')]/ancestor::div[contains(@class,'card')]"
    )

    phone = ""
    email = ""
    website = ""

    if contact_card.count():
        card = contact_card.first

        # website (first external link inside this card)
        links = card.locator("a[target='_blank']")
        for i in range(links.count()):
            href = links.nth(i).get_attribute("href")
            if href and href.startswith("http"):
                website = href.strip()
                break

        # email
        if card.locator("a[href^='mailto:']").count():
            email_href = card.locator("a[href^='mailto:']").first.get_attribute("href")
            email = _clean_email_from_href(email_href)

        # phone
        if card.locator("a[href^='tel:']").count():
            phone_href = card.locator("a[href^='tel:']").first.get_attribute("href")
            phone = _clean_phone_from_href(phone_href)
    else:
        # Fallback: look page-wide (but this might pick expo contact)
        if page.locator("a[href^='mailto:']").count():
            email_href = page.locator("a[href^='mailto:']").first.get_attribute("href")
            email = _clean_email_from_href(email_href)

        if page.locator("a[href^='tel:']").count():
            phone_href = page.locator("a[href^='tel:']").first.get_attribute("href")
            phone = _clean_phone_from_href(phone_href)

        # website: first external link
        all_links = page.locator("a[target='_blank']")
        for i in range(all_links.count()):
            href = all_links.nth(i).get_attribute("href")
            if href and href.startswith("http") and "vrexpogreece.com" not in href:
                website = href.strip()
                break

    return name, phone, email, website


# ---------------- AGENTS ---------------- #

def extract_agents(page):
    """
    Extract agents from the Agents block correctly by scanning each agent card
    and reading href values for phone & email.
    """

    agents = []

    print("🔎 Searching agents...")

    # Find the Agents section title
    agents_header = page.locator("//h4[contains(.,'Agents')]")

    if not agents_header.count():
        print("⚠ No Agents section found.")
        return agents

    # Find ALL agent cards that appear AFTER the Agents header
    agent_cards = page.locator("//h4[contains(.,'Agents')]/following::div[contains(@class,'card')]")

    print(f"📌 Found {agent_cards.count()} agent blocks")

    for i in range(agent_cards.count()):
        block = agent_cards.nth(i)

        # Extract agent name
        name = ""
        if block.locator("h6").count():
            name = block.locator("h6").first.inner_text().strip()

        # Extract agent role
        role = ""
        if block.locator("p.font-size-sm").count():
            role = block.locator("p.font-size-sm").first.inner_text().strip()

        # Extract phone
        phone = ""
        if block.locator("a[href^='tel:']").count():
            href = block.locator("a[href^='tel:']").first.get_attribute("href")
            phone = _clean_phone_from_href(href)

        # Extract email
        email = ""
        if block.locator("a[href^='mailto:']").count():
            href = block.locator("a[href^='mailto:']").first.get_attribute("href")
            email = _clean_email_from_href(href)

        # If a valid name found — add it
        if name:
            agents.append({
                "Agent Name": name,
                "Agent Role": role,
                "Agent Phone": phone,
                "Agent Email": email,
            })

    if agents:
        print(f"✅ Extracted {len(agents)} agents.")
    else:
        print("⚠ No agents extracted — but section was detected.")

    return agents


# ---------------- SCRAPING A COMPANY ---------------- #

def scrape_company(page, url):
    print(f"\n=== Scraping {url}")
    page.goto(url, wait_until="domcontentloaded")
    page.wait_for_timeout(2000)

    comp_name, comp_phone, comp_email, comp_site = extract_company_contact(page)
    agent_list = extract_agents(page)

    # If no agents found, still return one row with empty agent fields
    if not agent_list:
        agent_list = [
            {"Agent Name": "", "Agent Role": "", "Agent Phone": "", "Agent Email": ""}
        ]

    return comp_name, comp_phone, comp_email, comp_site, agent_list


# ---------------- MAIN ---------------- #

def main():
    print("🚀 Starting browser...")
    results = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        login(page)

        for link in COMPANY_URLS:
            (
                comp_name,
                comp_phone,
                comp_email,
                comp_site,
                agents,
            ) = scrape_company(page, link)

            for a in agents:
                results.append(
                    {
                        "Company URL": link,
                        "Company Name": comp_name,
                        "Company Phone": comp_phone,
                        "Company Email": comp_email,
                        "Company Website": comp_site,
                        "Agent Name": a["Agent Name"],
                        "Agent Role": a["Agent Role"],
                        "Agent Phone": a["Agent Phone"],
                        "Agent Email": a["Agent Email"],
                    }
                )

        browser.close()

    df = pd.DataFrame(results)
    df.to_excel("vrexpo_agents.xlsx", index=False)
    print("\n📌 DONE — saved vrexpo_agents.xlsx")


if __name__ == "__main__":
    main()
