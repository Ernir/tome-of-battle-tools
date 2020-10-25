export type Maybe<T> = T | null;
export type Exact<T extends { [key: string]: unknown }> = {
  [K in keyof T]: T[K];
};
/** All built-in and custom scalars, mapped to their actual values */
export type Scalars = {
  ID: string;
  String: string;
  Boolean: boolean;
  Int: number;
  Float: number;
};

export type Query = {
  __typename?: "Query";
  allManeuvers?: Maybe<Array<Maybe<ManeuverType>>>;
  singleManeuver?: Maybe<ManeuverType>;
};

export type QuerySingleManeuverArgs = {
  slug?: Maybe<Scalars["String"]>;
};

/** The core entity of the search engine, the one actually being searched for. Ties together all other game concepts. */
export type ManeuverType = {
  __typename?: "ManeuverType";
  id: Scalars["ID"];
  name: Scalars["String"];
  discipline: DisciplineType;
  maneuverType: ManeuverTypeType;
  descriptor: Array<DescriptorType>;
  level: Scalars["Int"];
  requirements: Scalars["Int"];
  action: ActionType;
  range: RangeType;
  target?: Maybe<TargetType>;
  area?: Maybe<AreaType>;
  effect?: Maybe<EffectType>;
  duration?: Maybe<DurationType>;
  savingThrow?: Maybe<SavingThrowType>;
  descriptiveText: Scalars["String"];
  slug: Scalars["String"];
  htmlDescription: Scalars["String"];
  page: Scalars["Int"];
  alternateVersion?: Maybe<ManeuverType>;
  hasErrataElsewhere: Scalars["Boolean"];
  maneuverSet: Array<ManeuverType>;
};

/** One of the nine disciplines described in the Tome of Battle - Book of Nine Swords. */
export type DisciplineType = {
  __typename?: "DisciplineType";
  id: Scalars["ID"];
  name: Scalars["String"];
  /** The URL fragment uniquely identifying the discipline. */
  slug: Scalars["String"];
  initiatorClasses: Array<InitiatorClassType>;
  maneuvers: Array<ManeuverType>;
};

/** An initiator character class, which has access to one or more disciplines. */
export type InitiatorClassType = {
  __typename?: "InitiatorClassType";
  id: Scalars["ID"];
  name: Scalars["String"];
  disciplines: Array<DisciplineType>;
};

/** A type of maneuver defined in the Tome of Battle, which affects how it interacts with some class features. */
export type ManeuverTypeType = {
  __typename?: "ManeuverTypeType";
  id: Scalars["ID"];
  name: Scalars["String"];
  maneuvers: Array<ManeuverType>;
};

/**
 * A maneuver descriptor, supplying meta-information about a maneuver. In the book, this is denoted by brackets, e.g.
 * [fire].
 */
export type DescriptorType = {
  __typename?: "DescriptorType";
  id: Scalars["ID"];
  name: Scalars["String"];
  maneuverSet: Array<ManeuverType>;
};

/** A D&D action type, defining the "time" it takes to use a maneuver. */
export type ActionType = {
  __typename?: "ActionType";
  id: Scalars["ID"];
  name: Scalars["String"];
  maneuverSet: Array<ManeuverType>;
};

/** The range at which a maneuver can be used. Can be a number of feet, or a definition such as "melee". */
export type RangeType = {
  __typename?: "RangeType";
  id: Scalars["ID"];
  name: Scalars["String"];
  /** Whether the range can be feasibly interpreted as a number. */
  isNumeric: Scalars["Boolean"];
  maneuverSet: Array<ManeuverType>;
};

/** Describes a valid target for a maneuver. */
export type TargetType = {
  __typename?: "TargetType";
  id: Scalars["ID"];
  description: Scalars["String"];
  maneuverSet: Array<ManeuverType>;
};

/** The area a maneuver affects, which tends to indicate the maneuver does not have a single :class:`Target`. */
export type AreaType = {
  __typename?: "AreaType";
  id: Scalars["ID"];
  description: Scalars["String"];
  maneuverSet: Array<ManeuverType>;
};

/** The effect produced by a maneuver. Most maneuvers do not produce effects, they have a :class:`Target`. */
export type EffectType = {
  __typename?: "EffectType";
  id: Scalars["ID"];
  description: Scalars["String"];
  maneuverSet: Array<ManeuverType>;
};

/**
 * A description of how long the maneuver lasts. Can be "instantaneous" or reference other rules, such as those which
 * last as stances do, or be expressed in terms of rounds.
 */
export type DurationType = {
  __typename?: "DurationType";
  id: Scalars["ID"];
  description: Scalars["String"];
  /** Whether the duration can be interpreted as a time range. */
  isTimed: Scalars["Boolean"];
  maneuverSet: Array<ManeuverType>;
};

/** A saving throw allowed by a maneuver. Most maneuvers do not allow saving throws, simply dealing damage on a hit. */
export type SavingThrowType = {
  __typename?: "SavingThrowType";
  id: Scalars["ID"];
  description: Scalars["String"];
  maneuverSet: Array<ManeuverType>;
};
