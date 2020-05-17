PRAGMA foreign_keys=OFF;

BEGIN TRANSACTION;
DROP TABLE IF EXISTS 'phyForm';
CREATE TABLE 'phyform' (
   "phyKey" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
   "shape"  NVARCHAR(6) NOT NULL
);
INSERT INTO 'phyform' VALUES (1,'Base');
INSERT INTO 'phyform' VALUES (2,'HT');
INSERT INTO 'phyform' VALUES (3,'Mobile');
COMMIT;

BEGIN TRANSACTION;
DROP TABLE IF EXISTS 'brand';
CREATE TABLE 'brand' (
   "brandKey" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
   "brandName" NVARCHAR(10) NOT NULL
);
INSERT INTO 'brand' VALUES(1,'Anytone');
INSERT INTO 'brand' VALUES(2,'Baofeng');
INSERT INTO 'brand' VALUES(3,'BTECH');
INSERT INTO 'brand' VALUES(4,'Icom');
INSERT INTO 'brand' VALUES(5,'Kenwood');
INSERT INTO 'brand' VALUES(6,'Yaesu');
COMMIT;

BEGIN TRANSACTION;
DROP TABLE IF EXISTS 'digMode';
CREATE TABLE 'digMode' (
   "digKey" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
   "mode"   NVARCHAR(10) NOT NULL
);
INSERT INTO 'digMode' VALUES (1,'None');
INSERT INTO 'digMode' VALUES (2,'DMR');
INSERT INTO 'digMode' VALUES (3,'DStar');
INSERT INTO 'digMode' VALUES (4,'NXDN');
INSERT INTO 'digMode' VALUES (5,'C4FM');
INSERT INTO 'digMode' VALUES (6,'P25');
COMMIT;

BEGIN TRANSACTION;
DROP TABLE IF EXISTS 'options';
CREATE TABLE 'options' (
   "optKey" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
   "rigndx" INTEGER NOT NULL,
   "options" NVARCHAR(15) NOT NULL
);
/* rigndx corresponds to rigs.rigNDX  */
/* a zero value is for menu           */
INSERT INTO 'options' VALUES (1,0,'APRS');
INSERT INTO 'options' VALUES (2,0,'Bluetooth');
INSERT INTO 'options' VALUES (3,0,'GPS');
INSERT INTO 'options' VALUES (4,0,'Radio Receiver');
INSERT INTO 'options' VALUES (5,0,'Full Duplex');
INSERT INTO 'options' VALUES (6,0,'Snapshot');
INSERT INTO 'options' VALUES (7,7,'APRS');
INSERT INTO 'options' VALUES (8,7,'Bluetooth');
INSERT INTO 'options' VALUES (9,7,'GPS');
INSERT INTO 'options' VALUES (10,6,'APRS');
INSERT INTO 'options' VALUES (11,6,'GPS');
INSERT INTO 'options' VALUES (12,6,'Snapshot');
COMMIT;

BEGIN TRANSACTION;
DROP TABLE IF EXISTS 'rigs';
CREATE TABLE 'rigs' (
   "rigNDX" INTEGER PRIMARY KEY NOT NULL,
   "model"  NVARCHAR(10) NOT NULL,
   "brand"  INTEGER NOT NULL,
   "shape"  INTEGER NOT NULL,
   "mode"   INTEGER NOT NULL,
   "msrp"   REAL NOT NULL,
   "vlink"  NVARCHAR(200)
);
INSERT INTO 'rigs' VALUES (1,'FT-450D',6,1,1,739.95,'https://www.yaesu.com/indexVS.cfm?cmd=DisplayProducts&ProdCatID=102&encProdID=870B3CA7CFCB61E6A599B0EFEA2217E4');
INSERT INTO 'rigs' VALUES (2,'TM-281A',5,3,1,149.95,'https://www.kenwood.com/usa/com/amateur/tm-281a/');
INSERT INTO 'rigs' VALUES (3,'AT-878UV',1,2,2,208.99,'https://www.bridgecomsystems.com/collections/amateur-handheld-radios/products/anytone-at-d878uv-dual-band-dmr-handheld-radio-w-gps-programming-cable');
INSERT INTO 'rigs' VALUES (4,'IC-718',4,1,1,679.95,'https://www.icomamerica.com/en/products/amateur/hf/718/default.aspx');
INSERT INTO 'rigs' VALUES (5,'FT-3DR',6,2,5,499.95,'https://www.yaesu.com/indexvs.cfm?cmd=DisplayProducts&ProdCatID=111&encProdID=84807B1262BFED6AC816544D94D310E3&DivisionID=65&isArchived=0');
INSERT INTO 'rigs' VALUES (6,'FT-2DR',6,2,5,393.99,'https://www.yaesu.com/indexVS.cfm?cmd=DisplayProducts&ProdCatID=111&encProdID=4A66D869E574453F343581B53E9FAB40&DivisionID=65&isArchived=0');
INSERT INTO 'rigs' VALUES (7,'AT-D578IIIPro',1,3,2,399.99,'https://www.bridgecomsystems.com/products/at-d578uv');
COMMIT;

