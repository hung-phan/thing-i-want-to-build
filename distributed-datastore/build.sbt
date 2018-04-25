organization in ThisBuild := "com.example"
version in ThisBuild := "1.0-SNAPSHOT"

// the Scala version that will be used for cross-compiled libraries
scalaVersion in ThisBuild := "2.12.4"

val macwire = "com.softwaremill.macwire" %% "macros" % "2.3.0" % "provided"
val scalaTest = "org.scalatest" %% "scalatest" % "3.0.4" % Test

lazy val `distributed-datastore` = (project in file("."))
  .aggregate(`distributed-datastore-api`, `distributed-datastore-impl`, `distributed-datastore-stream-api`, `distributed-datastore-stream-impl`)

lazy val `distributed-datastore-api` = (project in file("distributed-datastore-api"))
  .settings(
    libraryDependencies ++= Seq(
      lagomScaladslApi
    )
  )

lazy val `distributed-datastore-impl` = (project in file("distributed-datastore-impl"))
  .enablePlugins(LagomScala)
  .settings(
    libraryDependencies ++= Seq(
      lagomScaladslPersistenceCassandra,
      lagomScaladslKafkaBroker,
      lagomScaladslTestKit,
      macwire,
      scalaTest
    )
  )
  .settings(lagomForkedTestSettings: _*)
  .dependsOn(`distributed-datastore-api`)

lazy val `distributed-datastore-stream-api` = (project in file("distributed-datastore-stream-api"))
  .settings(
    libraryDependencies ++= Seq(
      lagomScaladslApi
    )
  )

lazy val `distributed-datastore-stream-impl` = (project in file("distributed-datastore-stream-impl"))
  .enablePlugins(LagomScala)
  .settings(
    libraryDependencies ++= Seq(
      lagomScaladslTestKit,
      macwire,
      scalaTest
    )
  )
  .dependsOn(`distributed-datastore-stream-api`, `distributed-datastore-api`)
