package com.example.hello.impl

import com.example.hello.api
import com.example.hello.api.{DistributeddatastoreService}
import com.lightbend.lagom.scaladsl.api.ServiceCall
import com.lightbend.lagom.scaladsl.api.broker.Topic
import com.lightbend.lagom.scaladsl.broker.TopicProducer
import com.lightbend.lagom.scaladsl.persistence.{EventStreamElement, PersistentEntityRegistry}

/**
  * Implementation of the DistributeddatastoreService.
  */
class DistributeddatastoreServiceImpl(persistentEntityRegistry: PersistentEntityRegistry) extends DistributeddatastoreService {

  override def hello(id: String) = ServiceCall { _ =>
    // Look up the distributed-datastore entity for the given ID.
    val ref = persistentEntityRegistry.refFor[DistributeddatastoreEntity](id)

    // Ask the entity the Hello command.
    ref.ask(Hello(id))
  }

  override def useGreeting(id: String) = ServiceCall { request =>
    // Look up the distributed-datastore entity for the given ID.
    val ref = persistentEntityRegistry.refFor[DistributeddatastoreEntity](id)

    // Tell the entity to use the greeting message specified.
    ref.ask(UseGreetingMessage(request.message))
  }


  override def greetingsTopic(): Topic[api.GreetingMessageChanged] =
    TopicProducer.singleStreamWithOffset {
      fromOffset =>
        persistentEntityRegistry.eventStream(DistributeddatastoreEvent.Tag, fromOffset)
          .map(ev => (convertEvent(ev), ev.offset))
    }

  private def convertEvent(helloEvent: EventStreamElement[DistributeddatastoreEvent]): api.GreetingMessageChanged = {
    helloEvent.event match {
      case GreetingMessageChanged(msg) => api.GreetingMessageChanged(helloEvent.entityId, msg)
    }
  }
}
