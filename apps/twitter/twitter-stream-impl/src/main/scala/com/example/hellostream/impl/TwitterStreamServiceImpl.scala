package com.example.hellostream.impl

import com.lightbend.lagom.scaladsl.api.ServiceCall
import com.example.hellostream.api.TwitterStreamService
import com.example.hello.api.TwitterService

import scala.concurrent.Future

/**
  * Implementation of the TwitterStreamService.
  */
class TwitterStreamServiceImpl(twitterService: TwitterService) extends TwitterStreamService {
  def stream = ServiceCall { hellos =>
    Future.successful(hellos.mapAsync(8)(twitterService.hello(_).invoke()))
  }
}
