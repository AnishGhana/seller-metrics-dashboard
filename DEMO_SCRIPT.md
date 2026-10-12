# 2-minute demo script

Open the locally running site and record your screen (not your face unless your instructor asks for it). Speak naturally; the following is a guide, not something you must memorize word-for-word.

> Hi, I’m **[your name]**, and this is my Research Milestone Django project, Seller Metrics Dashboard. The intended product helps sellers understand the performance of items they sell; it is not a storefront.
>
> I chose Django because it includes useful web-app features such as database models, forms, migrations, templates, and an admin interface. I used `uv` as the Python package manager and SQLite for this individual prototype.
>
> This is the dashboard. It summarizes total revenue, estimated profit, units sold, and how many products need restocking. It starts empty, so I’ll add a product.
>
> I’ll enter a product called Insulated Bottle, category Accessories, sale price 25 dollars, cost 9 dollars, inventory 15, and reorder level 4. After saving, it appears in the product-performance table.
>
> Now I’ll record a sale: three bottles at 25 dollars each. The dashboard now calculates 75 dollars in revenue and 48 dollars in estimated profit. It also reduces inventory automatically from 15 to 12. The sale is shown in Recent Sales.
>
> Finally, I’ll demonstrate input validation by trying to record 20 bottles even though only 12 are available. The app blocks it and explains why. This is an example of Django server-side form validation, not only visual UI behavior.
>
> For a full team version, I would use PostgreSQL, deploy with environment variables and production settings, and add user accounts so each seller sees only their own products. Thank you.

## Recording and upload

1. Use **Loom** (fastest): sign in at loom.com, select **Screen Only**, start recording, then stop and copy the share link. Or use Windows Snipping Tool → **Record**, which saves an MP4 locally.
2. Record 1–3 minutes. Show the browser, not VS Code. You may keep this script in another window, but do not read it mechanically.
3. Open the video link in an incognito/private window to confirm your instructor can view it.
4. Put the GitHub repository URL and the video URL into the required Issue in the **team repository**.
