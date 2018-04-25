package com.example.hellostream.impl

import com.lightbend.lagom.scaladsl.api.ServiceCall
import com.example.hellostream.api.DistributeddatastoreStreamService
import com.example.hello.api.DistributeddatastoreService

import scala.concurrent.Future

/**
  * Implementation of the DistributeddatastoreStreamService.
  */
class DistributeddatastoreStreamServiceImpl(distributeddatastoreService: DistributeddatastoreService) extends DistributeddatastoreStreamService {
  def stream = ServiceCall { hellos =>
    Future.successful(hellos.mapAsync(8)(distributeddatastoreService.hello(_).invoke()))
  }
}
