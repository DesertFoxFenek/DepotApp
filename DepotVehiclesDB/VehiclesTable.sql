--CREATE DATABASE DepotAppDb

--CREATE TABLE DepotAppDb.dbo.VehiclesTable
--(
--  [Id] INT NOT NULL PRIMARY KEY, --uniqe number of Vehicle
--  [Name] VARCHAR(50) NOT NULL,
--  [Model] VARCHAR(50),
--  [Type] VARCHAR(50) NOT NULL, -- Tram/Bus
--  [Depot] INT NOT NULL, -- 1 Zajezdnia Borek/2 Zajezdnia Olbin/3 Zajezdnia Gaj/4 Zajezdnia Obornicka
--)


--CREATE TABLE DepotAppDb.dbo.TimetableDB
--(
--  [Id] INT NOT NULL PRIMARY KEY, --line number
--  [StartPlace] VARCHAR(50),
--  [FinishPlace] VARCHAR(50),
--  [TurnAroundTime] TIME, --time needed to coplete one route
--  [Type] VARCHAR(50), --Tram line/Bus line
--)

--USE DepotAppDb;
--GO
--EXEC sp_rename 'dbo.TimetableDB.From', 'StartPlace', 'COLUMN';
--EXEC sp_rename 'dbo.TimetableDB.To', 'FinishPlace', 'COLUMN';