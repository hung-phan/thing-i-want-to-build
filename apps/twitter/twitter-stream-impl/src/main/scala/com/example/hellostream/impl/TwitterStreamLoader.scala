package com.example.hellostream.impl

import com.lightbend.lagom.scaladsl.api.ServiceLocator.NoServiceLocator
import com.lightbend.lagom.scaladsl.server._
import com.lightbend.lagom.scaladsl.devmode.LagomDevModeComponents
import play.api.libs.ws.ahc.AhcWSComponents
import com.example.hellostream.api.TwitterStreamService
import com.example.hello.api.TwitterService
import com.softwaremill.macwire._

class TwitterStreamLoader extends LagomApplicationLoader {

  override def load(context: LagomApplicationContext): LagomApplication =
    new TwitterStreamApplication(context) {
      override def serviceLocator = NoServiceLocator
    }

  override def loadDevMode(context: LagomApplicationContext): LagomApplication =
    new TwitterStreamApplication(context) with LagomDevModeComponents

  override def describeService = Some(readDescriptor[TwitterStreamService])
}

abstract class TwitterStreamApplication(context: LagomApplicationContext)
  extends LagomApplication(context)
    with AhcWSComponents {

  // Bind the service that this server provides
  override lazy val lagomServer = serverFor[TwitterStreamService](wire[TwitterStreamServiceImpl])

  // Bind the TwitterService client
  lazy val twitterService = serviceClient.implement[TwitterService]
}
