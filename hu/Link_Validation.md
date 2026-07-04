<!-- MT-DRAFT: machine translation; human review required -->

# <%= @title %>

A linkellenőrzés megpingeli az URL célhelyét, és teszteli a hibákat. Ez segít elkerülni a hibás és érvénytelen hivatkozásokat a közzétett dokumentumban, és különösen hasznos a bloggerek számára.

## Egyetlen hivatkozás ellenőrzése

![][1]

   [1]: images/validate_single.png @2x width=832px height=267px class=center

Kattintson és tartsa lenyomva a hivatkozást az előnézetben, amíg az villogni nem kezd, majd engedje fel a hivatkozás műveleti menüjének megnyitásához. A teszt futtatásához válassza a „Link érvényesítése” lehetőséget. Az eredmények a felugró ablakban jelennek meg.

## Az összes hivatkozás ellenőrzése

![][2]

   [2]: images/screenshots/mainwindow-feature-urlvalidate-crop.jpg @2x width=1089px height=300px class=center

Válassza az „Összes hivatkozás érvényesítése” (parancsikon {% kbd ctrl cmd L %}) lehetőséget a Fogaskerék menüből vagy a jobb gombbal kattintva. A dokumentumban lévő összes távoli hivatkozás ellenőrzésre kerül, és az eredmények egy előugró ablakban jelennek meg. A felugró ablakban egy hivatkozásra kattintva görgeti és kiemeli a megfelelő hivatkozást a dokumentumban.

Az érvényes URL-ek elrejthetők a felugró ablakban a tetején található "Érvényes elrejtése" gombbal. Ez csak azokat az URL-eket jeleníti meg, amelyek hibaállapotot adtak vissza.

Az Escape megnyomása elrejti az érvényesítési eredményeket. A {% kbd ctrl cmd L %} vagy a Fogaskerék menü segítségével ismét felfedhetők.

## Automatikus érvényesítés

Kapcsolja be az „URL-ek automatikus ellenőrzése frissítéskor” lehetőséget az Előnézet beállításainál (vagy a linkellenőrzési előugró ablak alján). Amikor a dokumentum betöltődik, a benne lévő hivatkozásokat a háttérben teszteljük. A párbeszédpanel csak akkor jelenik meg, ha hibák vannak.

Az előugró ablak letiltásához kapcsolja ki a beállításokban, vagy törölje a jelet a felugró ablak alján található négyzetből.