PRAGMA foreign_keys=OFF;

BEGIN TRANSACTION;
DROP TABLE IF EXISTS 'phyForm';
CREATE TABLE 'phyform' (
   "phyKey" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
   "shape"  NVARCHAR(6) NOT NULL
);
INSERT INTO 'phyform' (shape) VALUES ('Base');
INSERT INTO 'phyform' (shape) VALUES ('HT');
INSERT INTO 'phyform' (shape) VALUES ('Mobile');
COMMIT;

BEGIN TRANSACTION;
DROP TABLE IF EXISTS 'brand';
CREATE TABLE 'brand' (
   "brandKey" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
   "brandName" NVARCHAR(10) NOT NULL
);
INSERT INTO 'brand' (brandName) VALUES ('Anytone');
INSERT INTO 'brand' (brandName) VALUES ('Baofeng');
INSERT INTO 'brand' (brandName) VALUES ('BTECH');
INSERT INTO 'brand' (brandName) VALUES ('Icom');
INSERT INTO 'brand' (brandName) VALUES ('Kenwood');
INSERT INTO 'brand' (brandName) VALUES ('Yaesu');
COMMIT;

BEGIN TRANSACTION;
DROP TABLE IF EXISTS 'digMode';
CREATE TABLE 'digMode' (
   "digKey" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
   "mode"   NVARCHAR(10) NOT NULL
);
INSERT INTO 'digMode' (mode) VALUES ('None');
INSERT INTO 'digMode' (mode) VALUES ('DMR');
INSERT INTO 'digMode' (mode) VALUES ('DStar');
INSERT INTO 'digMode' (mode) VALUES ('NXDN');
INSERT INTO 'digMode' (mode) VALUES ('C4FM');
INSERT INTO 'digMode' (mode) VALUES ('P25');
COMMIT;

BEGIN TRANSACTION;
DROP TABLE IF EXISTS 'options';
CREATE TABLE 'options' (
   "optKey" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
   "rigndx" INTEGER NOT NULL,
   "option" NVARCHAR(15) NOT NULL
);
/*  rigndx corresponds to rigs.rigNDX               */
/*  This may change, need to think about this one.  */
/*  a zero value is for menu                        */
INSERT INTO 'options' (rigndx, option) VALUES (0,'APRS');
INSERT INTO 'options' (rigndx, option) VALUES (0,'Bluetooth');
INSERT INTO 'options' (rigndx, option) VALUES (0,'GPS');
INSERT INTO 'options' (rigndx, option) VALUES (0,'Radio Receiver (78-108 MHz)');
INSERT INTO 'options' (rigndx, option) VALUES (0,'Full Duplex');
INSERT INTO 'options' (rigndx, option) VALUES (0,'Snapshot');
INSERT INTO 'options' (rigndx, option) VALUES (0,'Band Scope');
INSERT INTO 'options' (rigndx, option) VALUES (0,'Voice Record');
INSERT INTO 'options' (rigndx, option) VALUES (7,'APRS');
INSERT INTO 'options' (rigndx, option) VALUES (7,'Bluetooth');
INSERT INTO 'options' (rigndx, option) VALUES (7,'GPS');
INSERT INTO 'options' (rigndx, option) VALUES (6,'APRS');
INSERT INTO 'options' (rigndx, option) VALUES (6,'GPS');
INSERT INTO 'options' (rigndx, option) VALUES (6,'Snapshot');
INSERT INTO 'options' (rigndx, option) VALUES (5,'APRS');
INSERT INTO 'options' (rigndx, option) VALUES (5,'Bluetooth');
INSERT INTO 'options' (rigndx, option) VALUES (5,'GPS');
INSERT INTO 'options' (rigndx, option) VALUES (5,'Radio Receiver (78-108 MHz)');
INSERT INTO 'options' (rigndx, option) VALUES (5,'Full Duplex');
INSERT INTO 'options' (rigndx, option) VALUES (5,'Snapshot');
INSERT INTO 'options' (rigndx, option) VALUES (5,'Band Scope');
INSERT INTO 'options' (rigndx, option) VALUES (5,'Voice Record');
INSERT INTO 'options' (rigndx, option) VALUES (3,'APRS');
INSERT INTO 'options' (rigndx, option) VALUES (3,'GPS');
INSERT INTO 'options' (rigndx, option) VALUES (3,'Voice Record');
COMMIT;

BEGIN TRANSACTION;
DROP TABLE IF EXISTS 'rigs';
CREATE TABLE 'rigs' (
   "rigNDX" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
   "model"  NVARCHAR(10) NOT NULL,
   "brand"  INTEGER NOT NULL,
   "shape"  INTEGER NOT NULL,
   "mode"   INTEGER NOT NULL,
   "msrp"   REAL NOT NULL,
   "vlink"  NVARCHAR(200)
);
INSERT INTO 'rigs' (model, brand, shape, mode, msrp, vlink) VALUES ('FT-450D','Yaesu',1,1,739.95,'https://www.yaesu.com/indexVS.cfm?cmd=DisplayProducts&ProdCatID=102&encProdID=870B3CA7CFCB61E6A599B0EFEA2217E4');
INSERT INTO 'rigs' (model, brand, shape, mode, msrp, vlink) VALUES ('TM-281A','Kenwood',3,1,149.95,'https://www.kenwood.com/usa/com/amateur/tm-281a/');
INSERT INTO 'rigs' (model, brand, shape, mode, msrp, vlink) VALUES ('AT-878UV','Anytone',2,2,208.99,'https://www.bridgecomsystems.com/collections/amateur-handheld-radios/products/anytone-at-d878uv-dual-band-dmr-handheld-radio-w-gps-programming-cable');
INSERT INTO 'rigs' (model, brand, shape, mode, msrp, vlink) VALUES ('IC-718','Icom',1,1,679.95,'https://www.icomamerica.com/en/products/amateur/hf/718/default.aspx');
INSERT INTO 'rigs' (model, brand, shape, mode, msrp, vlink) VALUES ('FT-3DR','Yaesu',2,5,499.95,'https://www.yaesu.com/indexvs.cfm?cmd=DisplayProducts&ProdCatID=111&encProdID=84807B1262BFED6AC816544D94D310E3&DivisionID=65&isArchived=0');
INSERT INTO 'rigs' (model, brand, shape, mode, msrp, vlink) VALUES ('FT-2DR','Yaesu',2,5,393.99,'https://www.yaesu.com/indexVS.cfm?cmd=DisplayProducts&ProdCatID=111&encProdID=4A66D869E574453F343581B53E9FAB40&DivisionID=65&isArchived=0');
INSERT INTO 'rigs' (model, brand, shape, mode, msrp, vlink) VALUES ('AT-D578IIIPro','Anytone',3,2,399.99,'https://www.bridgecomsystems.com/products/at-d578uv');
COMMIT;

