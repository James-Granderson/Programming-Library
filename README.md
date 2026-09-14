# Programming Library

## Purpose

The Programming Library is an attempt to build an ultimate, easily indexable library of programming knowledge.

The goal is to construct a system in which information can be **stored, related, retrieved, and expanded** from a small set of basic primitives.

The ambition is cognitive: something as prestigious as the Library of Alexandria, but built from the simplest possible foundations.

The information contained here is programming information: concepts, procedures, how-to's, observations, implementations, discoveries, solutions, and whatever else proves useful as the library develops.

The library is built around a simple principle:

> **You realize you need a thing, use a thing, and then store that thing.**

Information is therefore added based on use.

The Library records what becomes useful through actual interaction with programming. We try to avoid simply adding everything that might someday be useful all at

once without proper exposure to the mechanism through practice. 

---

## The Schema

The fundamental problem with a large information library is **retrieval**.

As information accumulates, a simple folder hierarchy eventually becomes insufficient. A piece of information may belong simultaneously to a language, an environment, an object, an action, a concept, and a particular method of use.

Therefore, the Programming Library is organized around a **schema of relations** rather than a single hierarchy.

The schema provides the primitives through which information can be described and connected.

The current Programming Dictionary schema is outlined as such:

* **Actions**
* **Classifications**
* **Concepts**
* **Environments**
* **Objects**
* **Path Types**

These categories form the vocabulary through which library information can be indexed.

The schema is deliberately small.

The objective is to create a sufficiently expressive set of primitives from which complex relationships can be constructed rather than an enormous, ambiguous taxonomy.

---

## Relations

The schema allows information to be related in multiple directions.

A search does not need to follow a single path through a directory tree.

It can be constructed similarly to a sentence.

A query may begin with an action and move toward an object:

```text
ACTION → OBJECT → ENVIRONMENT
```

or begin with an environment and move toward a concept:

```text
ENVIRONMENT → CONCEPT → ACTION
```

or begin with an object and work backward:

```text
OBJECT → ACTION → CONCEPT
```

The system therefore supports both **forward and backward reasoning**.

Information can be traversed:

* top-down
* bottom-up
* front-to-back
* back-to-front
* across related classifications
* through multiple connected paths


The hierarchy allots possible paths through the relationships and should not be confused as a relationship itself.

---

## Keys and Collisions

A major requirement of the library is that information remain uniquely addressable.

Keys are therefore used to prevent collisions between entries.

The important distinction is that the **objects described by the schema are not themselves the keys**.

An object may appear in many relationships without becoming the identifier of the information describing it.

The key identifies the entry.

The schema describes what the entry **is related to**.

This distinction allows the same programming object, concept, action, or environment to participate in many different entries without collapsing those entries into one another.

---

## Information as Relations

The library should be thought of less as a collection of isolated documents and more as a network of related information.

For example, a single programming problem might involve:

```text
Environment
    ↓
Object
    ↓
Action
    ↓
Concept
    ↓
Individual Procedure
```

Another problem may begin from the individual procedure and lead backward toward the environment in which it applies.

The same information can therefore be discovered from different starting points.

This is the central advantage of the schema.

---

## Information Added by Use

The library grows organically.

There is no requirement that every possible programming concept be documented before the system becomes useful.

A programming problem creates a need.

The need leads to discovery.

The discovered information is used.

Once the solution proves useful, it becomes library information.

The next time the problem appears, the information can be retrieved rather than rediscovered from scratch.

The library therefore becomes a cumulative memory of programming experience.

---

## The Programming Dictionary

The Programming Dictionary provides the controlled vocabulary used by the library.

Its purpose is to make information consistently indexable.

Natural-language descriptions can vary enormously.

The Dictionary is not intended to replace natural language.

The schema provides stable primitives with which those descriptions can be connected.

This allows a human-readable explanation and a machine-readable structure to coexist.

---

## Hypsos

**Hypsos** is the automation system associated with the Programming Library.

Its purpose is to help maintain and expand the library as information accumulates.

Hypsos operates within the established schema rather than inventing arbitrary classifications for individual entries.

The long-term objective is for the library to become increasingly capable of organizing its own accumulated knowledge while preserving the simplicity of its underlying primitives.

The system should grow in complexity through **relationships**, not through unnecessary complexity in the primitives themselves.

---

## Design Philosophy

The Programming Library follows several principles.

### 1. Small primitives

The underlying schema should remain as simple as possible.

### 2. Rich relationships

Complexity should emerge from relationships between primitives rather than from endlessly expanding the primitive vocabulary.

### 3. Retrieval over decoration

Information is valuable because it can be found and used.

### 4. Use before storage

Knowledge enters the library because it proved useful and was tested.

### 5. Preserve distinctions

Different concepts, objects, environments, actions, and procedures should not be collapsed merely because they appear similar.

### 6. Multiple paths

Information should be retrievable from different directions.

### 7. Accumulation

Every useful discovery should have the potential to become part of the permanent library.

---

## The Long-Term Goal

The ultimate goal is a programming library whose size does not make it less useful.

Normally, information systems become harder to navigate as they grow.

This library should do the opposite.

As more information is added, more relationships become available.

As more relationships become available, more paths to information become possible.

The result should be a growing computational memory of programming knowledge.

The ambition is simple:

**Build an immense software library from very small primitives.**
